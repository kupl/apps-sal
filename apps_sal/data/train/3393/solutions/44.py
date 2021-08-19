import math


def list_squared(m, n):
    final = []
    for i in range(m, n + 1):
        results = []
        for j in range(1, int(math.sqrt(i)) + 1):
            if i % j == 0:
                if int(i / j) != j:
                    results.append(int(i / j) ** 2)
                results.append(j ** 2)
        summ = sum(results)
        if math.sqrt(summ).is_integer():
            final.append([i, summ])
    return final
