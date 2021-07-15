n = int(input())
numbers = [0] * n
used = set()
for i in range(n):
    for j in range(max(list(map(int, input().split()))), n + 1):
        if j not in used:
            used.add(j)
            numbers[i] = j
            break
print(' '.join(map(str, numbers)))
