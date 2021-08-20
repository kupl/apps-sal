(n, t) = (int(input()), list(map(int, input().split())))
print(max(max(t), (sum(t) - 1) // (n - 1) + 1))
