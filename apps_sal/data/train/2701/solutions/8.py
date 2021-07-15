get_score = lambda arr, acc=__import__("itertools").accumulate: sum(map(lambda ln, lv: [0, 40, 100, 300, 1200][ln] * (lv//10 + 1), arr, acc([0] + arr)))
