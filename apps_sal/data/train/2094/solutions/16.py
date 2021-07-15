N = int(input())
S = input()

num_zeros = 0
num_ones = 0

for w in S:
    if w == 'z':
        num_zeros += 1
    if w == 'n':
        num_ones += 1

foo = ['1' for _ in range(num_ones)] + ['0' for _ in range(num_zeros)]
print(" ".join(foo))


