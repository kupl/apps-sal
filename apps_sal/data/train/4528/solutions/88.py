def my_languages(results):
    results_1 = [i for i in results.items()]
    results_1 = [[i[0], i[1]] for i in results_1 if i[1] >= 60]
    results_swap = {i[1]: i[0] for i in results_1}
    results_ksort = sorted(results_swap, reverse=True)
    results_done = [results_swap.get(i) for i in results_ksort]
    return results_done
