notes = ['a4', 'b4', 'c4', 'd4', 'e4', 'f4', 'g4']
durations = [1, 2, 4, 8]

g_minor_scale = ['g', 'a', 'a#', 'c', 'd', 'd#', 'f']

building_blocks = [
    # Beethoven
    (('e4', 8), ('f#4', 8), ('g4*', 4), ('f#4', 8), ('e4', 8), ('d#4*', 4)),  # Symphony No. 5
    (('e4', 8), ('g4', 8), ('b4', 8), ('e5', 8), ('b4', 8), ('g4', 8)),  # Moonlight Sonata
    (('c4', 8), ('d4', 8), ('e4', 8), ('f4', 8), ('g4', 8), ('a4', 8)),  # Ode to Joy
    (('a3', 8), ('g3', 8), ('f3', 8), ('e3', 8), ('d3', 8), ('c3', 8)),  # Für Elise
    (('e4', 8), ('g#4', 8), ('b4', 8), ('e5', 8), ('b4', 8), ('g#4', 8)),  # Moonlight Sonata (variation)

    # Mozart
    (('g4', 8), ('a4', 8), ('b4', 8), ('c5', 8), ('d5', 8), ('e5', 8)),  # Symphony No. 40
    (('c4', 8), ('d4', 8), ('e4', 8), ('f4', 8), ('g4', 8), ('a4', 8)),  # Eine kleine Nachtmusik
    (('d4', 8), ('f#4', 8), ('g4', 8), ('b4', 8), ('d5', 8), ('g5', 8)),  # Turkish March
    (('f3', 8), ('g3', 8), ('a3', 8), ('b3', 8), ('c4', 8), ('d4', 8)),  # Symphony No. 25
    (('g4', 8), ('a4', 8), ('b4', 8), ('c5', 8), ('d5', 8), ('e5', 8), ('f#5', 8), ('g5', 8)),  # Symphony No. 40 (variation)

    # Bach
    (('f4', 8), ('e4', 8), ('d4', 8), ('c4', 8), ('b3', 8), ('c4', 8)),  # Air on the G String
    (('g4', 8), ('b4', 8), ('d5', 8), ('f5', 8), ('d5', 8), ('b4', 8)),  # Jesu, Joy of Man's Desiring
    (('d4', 8), ('f#4', 8), ('a4', 8), ('d5', 8), ('a4', 8), ('f#4', 8)),  # Brandenburg Concerto No. 3
    (('g#3', 8), ('a3', 8), ('b3', 8), ('c4', 8), ('d4', 8), ('e4', 8)),  # Toccata and Fugue in D minor
    (('c4', 8), ('d4', 8), ('e4', 8), ('f4', 8), ('g4', 8), ('a4', 8), ('b4', 8), ('c5', 8)),  # Pachelbel's Canon

    # Chopin
    (('c#4', 8), ('e4', 8), ('g#4', 8), ('c#5', 8), ('g#4', 8), ('e4', 8)),  # Revolutionary Étude
    (('e4', 8), ('g#4', 8), ('b4', 8), ('e5', 8), ('b4', 8), ('g#4', 8)),  # Nocturne Op. 9 No. 2
    (('c#3', 8), ('e3', 8), ('g#3', 8), ('c#4', 8), ('g#3', 8), ('e3', 8)),  # Étude Op. 10 No. 4
    (('e5', 8), ('g#5', 8), ('b5', 8), ('e6', 8), ('b5', 8), ('g#5', 8)),   # Ballade No. 1 in G minor
    (('a3', 8), ('c#4', 8), ('e4', 8), ('a4', 8), ('e4', 8), ('c#4', 8)),  # Fantaisie-Impromptu Op. 66

    # Additional fragments
    (('c4', 8), ('d4', 8), ('e4', 8), ('f4', 8), ('e4', 8), ('d4', 8), ('c4', 8)),  # Simple ascending scale
    (('c4', 8), ('b3', 8), ('a3', 8), ('g3', 8), ('f3', 8), ('e3', 8), ('d3', 8)),  # Simple descending scale
    (('c4', 4), ('g3', 4), ('c4', 4), ('e3', 4), ('g3', 4), ('c4', 4)),  # C major arpeggio
    (('c4', 4), ('e4', 4), ('g4', 4), ('c5', 4), ('g4', 4), ('e4', 4)),  # C major chord

    # Longer passages
    (('g4', 8), ('a4', 8), ('b4', 8), ('c5', 8), ('d5', 8), ('c5', 8), ('b4', 8), ('a4', 8), ('g4', 8)),  # Arpeggio sequence
    (('c4', 8), ('d4', 8), ('e4', 8), ('f4', 8), ('g4', 8), ('f4', 8), ('e4', 8), ('d4', 8), ('c4', 8)),  # Descending sequence
    (('e4', 8), ('g4', 8), ('b4', 8), ('d5', 8), ('g4', 8), ('a4', 8), ('b4', 8), ('d5', 8), ('f#5', 8)), # Broken chord sequence

    (('c4', 8), ('d4', 8), ('e4', 8), ('f4', 8), ('g4', 8), ('a4', 8), ('b4', 8), ('c5', 8), ('d5', 8), ('e5', 8), ('f5', 8), ('g5', 8)),  # Beethoven's Ode to Joy ending
    (('e4', 8), ('f#4', 8), ('g4', 8), ('a4', 8), ('b4', 8), ('c5', 8), ('d5', 8), ('e5', 8), ('f#5', 8), ('g5', 8), ('a5', 8), ('b5', 8)),  # Beethoven's Symphony No. 5 ending

    # Mozart endings
    (('g4', 8), ('a4', 8), ('b4', 8), ('c5', 8), ('d5', 8), ('e5', 8), ('f#5', 8), ('g5', 8), ('a5', 8), ('b5', 8), ('c6', 8), ('d6', 8)),  # Mozart's Symphony No. 40 ending
    (('e4', 8), ('d4', 8), ('c4', 8), ('b3', 8), ('a3', 8), ('g3', 8), ('f3', 8), ('e3', 8), ('d3', 8), ('c3', 8), ('b2', 8), ('a2', 8))  # Mozart's Eine kleine Nachtmusik ending
]