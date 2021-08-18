t = int(input())
for i in range(t):
    n, b = map(int, input().split(" "))
    num = n // b
    final = [i * (n - b * i) for i in range(num + 1)]
    print(max(final))
