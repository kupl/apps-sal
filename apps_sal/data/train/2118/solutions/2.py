s = 0
for t in range(int(input())):
    s ^= int((8 * int(input()) + 1) ** 0.5 - 1) // 2
print(['YES', 'NO'][s > 0])
