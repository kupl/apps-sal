N = int(input())
(sp, psp) = (0, 0)
for i in range(1, 10 ** 6 + 1):
    l = [int(j) for j in str(i)]
    prod = 1
    for k in l:
        prod *= k
    if prod == N and '1' not in str(i):
        sp += 1
    elif prod == N and '1' in str(i):
        psp += 1
print(sp, psp)
