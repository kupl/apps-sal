memo = [[0, 0, 0, 0], [1, 1, 1, 1]]
for i in range(3, 1000000, 2):
    memo.append([j for j in range(i ** 2, i ** 2 - (i - 1) * 3 - 1, -i + 1)][::-1])

def branch(n):
    layer = int((1 + (n - 1)**0.5)//2 + 1)
    for branch, coner_number in enumerate(memo[layer]):
        if n <= coner_number:
            return branch
