N = int(input())
A = list(map(int, input().split()))
X = 0
for a in A:
    X ^= a
print((*[X ^ a for a in A]))
