str = input()

bset = []

bno = 0

for c in str:
    if c == 'b':
        bno += 1
    else:
        bset += [bno]
        bno = 0
bset += [bno]

ans = 0
acc = 0

for n in reversed(bset[1:]):
    ans += acc + n
    acc *= 2
    acc += 2 * n
    acc %= 1000000007
    ans %= 1000000007

print(ans)
