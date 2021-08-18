t = int(input())
for _ in range(t):
    s = input()
    a = s.count('0')
    b = s.count('1')
    if(len(s) % 2 == 1 or a == 0 or b == 0):
        ans = -1
    else:
        ans = abs(a - b) // 2
    print(ans)
