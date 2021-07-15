get_grade = lambda *scores: [letter for letter in {'A': (90, 100), 'B': (80, 90), 'C': (70, 80), 'D': (60, 70), 'F': (0, 60)} if {'A': (90, 100), 'B': (80, 90), 'C': (70, 80), 'D': (60, 70), 'F': (0, 60)}[letter][0] <= sum(scores) / len(scores) <= {'A': (90, 100), 'B': (80, 90), 'C': (70, 80), 'D': (60, 70), 'F': (0, 60)}[letter][1]][0]

# what even is this monstosity honestly

