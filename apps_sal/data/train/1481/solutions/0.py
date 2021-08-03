t = int(input())
for i in range(t):
    s = input()
    zeroes = s.count('0')
    ones = s.count('1')
    if (len(s) % 2 == 1 or zeroes == 0 or ones == 0):
        ans = -1
    else:
        ans = abs(zeroes - ones) // 2
    print(ans)
