import random
import sys
sys.path.append('../music/')
import muser as ms
import building_blocks as bb

class GeneticAlgorithm:
    def __init__(self, population_size, generations, mutation_rate, individual_length):
        self.population_size = population_size
        self.generations = generations
        self.mutation_rate = mutation_rate
        self.individual_length = individual_length

    def generate_individual(self):
        track = []
        while len(track) < self.individual_length:
            block = random.choice(bb.building_blocks)
            track.extend(block)
        return track[:self.individual_length]

    def initialize_population(self):
        return [self.generate_individual() for _ in range(self.population_size)]

    def fitness(self, composition):
        duration_variety = len(set(duration for _, duration in composition))
        note_variety = len(set(note for note, _ in composition))
        note_scale_matches = sum(note[:-1] in bb.c_major_scale for note, _ in composition)
        rhythmic_diversity = len(set(duration for _, duration in composition))
        repetition_penalty = -sum(composition[i] == composition[i + 1] for i in range(len(composition) - 1))

        ending_notes = [note[:-1] for block in bb.building_blocks[-4:] for note, _ in block]
        ending_bonus = sum(1 for note, _ in composition[-len(ending_notes):] if note in ending_notes)

        return duration_variety + note_variety + note_scale_matches + rhythmic_diversity + repetition_penalty + ending_bonus

    def selection(self, population, fitnesses):
        best_indices = sorted(range(len(fitnesses)), key=lambda i: fitnesses[i], reverse=True)[:2]
        return [population[i] for i in best_indices]
    
    def crossover(self, parent1, parent2):
        crossover_point = random.randint(1, len(parent1) - 1)
        child1 = parent1[:crossover_point] + parent2[crossover_point:]
        child2 = parent2[:crossover_point] + parent1[crossover_point:]
        return child1, child2

    def mutate(self, composition):
        if random.random() < self.mutation_rate:
            index = random.randint(0, len(composition) - 1)
            composition[index] = (random.choice(bb.notes), random.choice(bb.durations))
        if random.random() < self.mutation_rate:
            block = random.choice(bb.building_blocks)
            index = random.randint(0, len(composition) - len(block))
            composition[index:index+len(block)] = block
        return composition

    def run(self):
        population = self.initialize_population()

        for generation in range(self.generations):
            fitnesses = [self.fitness(composition) for composition in population]

            new_population = []
            while len(new_population) < self.population_size:
                parents = self.selection(population, fitnesses)
                offspring = self.crossover(*parents)
                new_population.extend(self.mutate(child) for child in offspring)

            population = new_population[:self.population_size]

            best_fitness = max(fitnesses)
            print(f'Generation {generation + 1}, Best Fitness: {best_fitness}')

        best_composition = population[fitnesses.index(max(fitnesses))]
        bass_composition = [(note[:-1] + "2", duration) for note, duration in best_composition]
        return best_composition, bass_composition