def nQueen(n):
    if n <= 3:
        return [[], [0]][n == 1]
    mod = n % 6
    odd = list(range(1, n + 1, 2))
    even = list(range(2, n + 1, 2))
    if mod == 2:
        odd[:2] = odd[:2][::-1]
        odd.append(odd.pop(2))
    elif mod == 3:
        even.append(even.pop(0))
        odd.extend([odd.pop(0), odd.pop(0)])
    return [i - 1 for i in even + odd]
