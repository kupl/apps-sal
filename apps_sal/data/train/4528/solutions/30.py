def my_languages(results):
    results_lookup = {v: k for k, v in results.items()}
    board = [score for score in results.values() if score >= 60]
    board.sort(reverse=True)
    return [results_lookup[k] for k in board]
