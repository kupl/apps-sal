N = int(input())
A = list(map(int, input().split()))
all = 0
for a in A:
    all ^= a
for a in A:
    print(all ^ a, end=" ")
