N = int(input())
A = list([int(x) for x in input().split()])

xor_base = A[0]
for a in A[1:]:
    xor_base ^= a

result = []
for a in A:
    result.append(a ^ xor_base)

print((*result))
