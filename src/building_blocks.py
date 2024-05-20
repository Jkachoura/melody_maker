notes = ['a4', 'b4', 'c4', 'd4', 'e4', 'f4', 'g4']
durations = [1, 2, 4, 8]

g_minor_scale = ['g', 'a', 'a#', 'c', 'd', 'd#', 'f']
c_major_scale = ['c', 'd', 'e', 'f', 'g', 'a', 'b']

building_blocks = [
    # Beethoven's fragments
    (('e4', 8), ('f#4', 8), ('g4*', 4), ('f#4', 8), ('e4', 8), ('d#4*', 4)),  # Beethoven's Symphony No. 5
    (('e4', 8), ('f#4', 8), ('g4', 8), ('a4', 8), ('b4', 8), ('c5', 8)),
    (('g4', 8), ('f4', 8), ('e4', 8), ('d4', 8), ('c4', 8), ('b3', 8)),  # Beethoven's Für Elise
    (('a3', 8), ('g3', 8), ('f3', 8), ('e3', 8), ('d3', 8), ('c3', 8)),
    (('e4', 8), ('g#4', 8), ('b4', 8), ('e5', 8), ('b4', 8), ('g#4', 8)),  # Beethoven's Moonlight Sonata
    (('e4', 8), ('g#4', 8), ('b4', 8), ('d5', 8), ('f5', 8), ('g#5', 8)),
    (('c4', 8), ('d4', 8), ('e4', 8), ('f4', 8), ('g4', 8), ('a4', 8)),  # Beethoven's Ode to Joy
    (('b4', 8), ('c5', 8), ('d5', 8), ('e5', 8), ('f5', 8), ('g5', 8)),

    # Mozart's fragments
    (('g4', 8), ('a4', 8), ('b4', 8), ('a4', 8), ('g4', 8), ('f#4', 8)),  # Mozart's Symphony No. 40
    (('e4', 8), ('f#4', 8), ('g4', 8), ('a4', 8), ('b4', 8), ('c5', 8)),
    (('e4', 8), ('d4', 8), ('c4', 8), ('b3', 8), ('a3', 8), ('b3', 8)),  # Mozart's Eine kleine Nachtmusik
    (('c4', 8), ('d4', 8), ('e4', 8), ('f4', 8), ('g4', 8), ('a4', 8)),
    (('d4', 8), ('e4', 8), ('f#4', 8), ('g4', 8), ('a4', 8), ('b4', 8)),  # Mozart's Turkish March
    (('c#5', 8), ('d5', 8), ('e5', 8), ('f5', 8), ('g5', 8), ('a5', 8)),
    (('c4', 8), ('b3', 8), ('a3', 8), ('g3', 8), ('f3', 8), ('e3', 8)),  # Mozart's Symphony No. 25
    (('d3', 8), ('c3', 8), ('b2', 8), ('a2', 8), ('g2', 8), ('f2', 8)),

    # Bach's fragments
    (('f4', 8), ('e4', 8), ('d4', 8), ('c4', 8), ('b3', 8), ('c4', 8)),  # Bach's Air on the G String
    (('d4', 8), ('e4', 8), ('f4', 8), ('g4', 8), ('a4', 8), ('b4', 8)),
    (('d4', 8), ('f#4', 8), ('a4', 8), ('d5', 8), ('a4', 8), ('f#4', 8)),  # Bach's Brandenburg Concerto No. 3
    (('d4', 8), ('f#4', 8), ('g4', 8), ('b4', 8), ('d5', 8), ('g5', 8)),
    (('g4', 8), ('b4', 8), ('d5', 8), ('f5', 8), ('d5', 8), ('b4', 8)),  # Bach's Jesu, Joy of Man's Desiring
    (('g4', 8), ('b4', 8), ('c5', 8), ('e5', 8), ('g5', 8), ('b5', 8)),
    (('f4', 8), ('e4', 8), ('d4', 8), ('c4', 8), ('b3', 8), ('a3', 8)),  # Bach's Toccata and Fugue in D minor
    (('g#3', 8), ('a3', 8), ('b3', 8), ('c4', 8), ('d4', 8), ('e4', 8)),

    # Chopin's fragments
    (('c#4', 8), ('e4', 8), ('g#4', 8), ('c#5', 8), ('g#4', 8), ('e4', 8)),  # Chopin's Revolutionary Étude
    (('e4', 8), ('g#4', 8), ('b4', 8), ('e5', 8), ('b4', 8), ('g#4', 8)),  # Chopin's Nocturne Op. 9 No. 2
    (('c#3', 8), ('e3', 8), ('g#3', 8), ('c#4', 8), ('g#3', 8), ('e3', 8)),  # Chopin's Étude Op. 10 No. 4
    (('e5', 8), ('g#5', 8), ('b5', 8), ('e6', 8), ('b5', 8), ('g#5', 8)),   # Chopin's Ballade No. 1 in G minor

    # Beethoven endings
    (('c4', 8), ('d4', 8), ('e4', 8), ('f4', 8), ('g4', 8), ('a4', 8), ('b4', 8), ('c5', 8), ('d5', 8), ('e5', 8), ('f5', 8), ('g5', 8)),  # Beethoven's Ode to Joy ending
    (('e4', 8), ('f#4', 8), ('g4', 8), ('a4', 8), ('b4', 8), ('c5', 8), ('d5', 8), ('e5', 8), ('f#5', 8), ('g5', 8), ('a5', 8), ('b5', 8)),  # Beethoven's Symphony No. 5 ending

    # Mozart endings
    (('g4', 8), ('a4', 8), ('b4', 8), ('c5', 8), ('d5', 8), ('e5', 8), ('f#5', 8), ('g5', 8), ('a5', 8), ('b5', 8), ('c6', 8), ('d6', 8)),  # Mozart's Symphony No. 40 ending
    (('e4', 8), ('d4', 8), ('c4', 8), ('b3', 8), ('a3', 8), ('g3', 8), ('f3', 8), ('e3', 8), ('d3', 8), ('c3', 8), ('b2', 8), ('a2', 8))  # Mozart's Eine kleine Nachtmusik ending
]
