n, l = list(map(int, input().split()))

s = []
for i in range(n):
    s.append(input())


print(("".join(sorted(s))))
