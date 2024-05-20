import random
import sys

sys.path.append('../music/')
import muser as ms
import building_blocks as bb


class GeneticAlgorithm:
    def __init__(self, population_size, generations, mutation_rate, individual_length):
        """
        Initializes the GeneticAlgorithm with given parameters.

        Args:
            population_size (int): Number of individuals in the population.
            generations (int): Number of generations to run the algorithm.
            mutation_rate (float): Probability of mutation for each individual.
            individual_length (int): Length of each individual composition.
        """
        self.population_size = population_size
        self.generations = generations
        self.mutation_rate = mutation_rate
        self.individual_length = individual_length

    def generate_individual(self):
        """
        Generates a single individual by randomly selecting building blocks until the desired length is reached.

        Returns:
            list: A list of tuples representing a musical composition.
        """
        track = []
        while len(track) < self.individual_length:
            block = random.choice(bb.building_blocks)
            track.extend(block)
        return track[:self.individual_length]

    def initialize_population(self):
        """
        Initializes the population with randomly generated individuals.

        Returns:
            list: A list of individuals representing the initial population.
        """
        return [self.generate_individual() for _ in range(self.population_size)]

    def fitness(self, composition):
        """
        Evaluates the fitness of a given composition based on various musical criteria.

        Args:
            composition (list): A list of tuples representing a musical composition.

        Returns:
            int: A fitness score indicating the quality of the composition.
        """
        # Initialize fitness components
        duration_variety = len(set(duration for _, duration in composition))
        note_variety = len(set(note for note, _ in composition))
        note_scale_matches = sum(note[:-1] in bb.g_minor_scale for note, _ in composition)
        rhythmic_diversity = len(set(duration for _, duration in composition))
        repetition_penalty = -sum(composition[i] == composition[i + 1] for i in range(len(composition) - 1))

        # Calculate ending bonus
        ending_notes = [note[:-1] for block in bb.building_blocks[-4:] for note, _ in block]
        ending_bonus = sum(1 for note, _ in composition[-len(ending_notes):] if note in ending_notes)

        # Enhance ending quality
        ending_quality = sum(1 for end_block in bb.building_blocks[-4:] if end_block[-4:] == composition[-4:])
        ending_bonus += ending_quality * 2  # Give more weight to matching endings

        # reward sequences
        sequence_bonus = 0
        for i in range(len(composition) - 2):
            if composition[i:i + 3] in bb.building_blocks:
                sequence_bonus += 1

        # Combine fitness components with weights based on importance
        fitness_score = (
            duration_variety * 1 + 
            note_variety * 1 + 
            note_scale_matches * 2 + 
            rhythmic_diversity * 1 + 
            repetition_penalty * (-1) + 
            ending_bonus * 2 +
            sequence_bonus * 3
        )

        return fitness_score


    def selection(self, population, fitnesses):
        """
        Selects the best individuals from the population based on their fitness scores.

        Args:
            population (list): The current population of individuals.
            fitnesses (list): The fitness scores of the individuals in the population.

        Returns:
            list: A list of the best individuals.
        """
        # Select the top 10% of individuals
        best_indices = sorted(range(len(fitnesses)), key=lambda i: fitnesses[i], reverse=True)[:int(0.1 * self.population_size)]
        return [population[i] for i in best_indices]

    def crossover(self, parent1, parent2):
        """
        Performs crossover between two parent compositions to produce two offspring.

        Args:
            parent1 (list): The first parent composition.
            parent2 (list): The second parent composition.

        Returns:
            tuple: Two new compositions created by combining parts of the parents.
        """
        if random.random() < 0.6:
            # Choose crossover points
            index1, index2, index3, index4 = sorted(random.sample(range(len(parent1)), 4))
            # Create offspring by swapping sections of parents
            child1 = parent1[:index1] + parent2[index1:index2] + parent1[index2:index3] + parent2[index3:index4] + parent1[index4:]
            child2 = parent2[:index1] + parent1[index1:index2] + parent2[index2:index3] + parent1[index3:index4] + parent2[index4:]
        else:
            # If crossover doesn't occur, offspring are identical to parents
            child1, child2 = parent1, parent2
        return child1, child2

    def mutate(self, composition):
        """
        Applies mutation to a given composition with a certain probability.

        Args:
            composition (list): A musical composition to mutate.

        Returns:
            list: The mutated composition.
        """
        if random.random() < self.mutation_rate:
            # Choose a random note in the composition to mutate
            index = random.randint(0, len(composition) - 1)
            # Mutate the chosen note by replacing it with a random note
            composition[index] = (random.choice(bb.notes), random.choice(bb.durations))
        return composition

    def run(self):
        """
        Executes the genetic algorithm to evolve the population over multiple generations.

        Returns:
            tuple: The best composition found and its corresponding bass composition.
        """
        population = self.initialize_population()
        fitnesses_list = []

        for generation in range(self.generations):
            # Evaluate fitness of each individual in the population
            fitnesses = [self.fitness(composition) for composition in population]
            # Track best fitness for this generation
            best_fitness = max(fitnesses)
            fitnesses_list.append(best_fitness)
            print(f'Generation {generation + 1}, Best Fitness: {best_fitness}')
            # Select the best individuals from the population
            new_population = self.selection(population, fitnesses)
            # Generate new individuals through crossover and mutation
            while len(new_population) < self.population_size:
                parent1, parent2 = random.choices(population, weights=fitnesses, k=2)
                child1, child2 = self.crossover(parent1, parent2)
                new_population.extend([self.mutate(child1), self.mutate(child2)])
            # Update population for next generation
            population = new_population[:self.population_size]

        # Retrieve the best composition found
        best_composition = population[fitnesses.index(max(fitnesses))]
        # Generate bass composition for more tasteful results
        bass_composition = [(note[:-1] + "2", duration) for note, duration in best_composition]
        return best_composition, bass_composition, fitnesses_list
