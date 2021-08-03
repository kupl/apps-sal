# cook your dish here
for u in range(int(input())):
    s = input()
    cnt0 = s.count('0')
    cnt1 = s.count('1')
    if len(s) % 2 != 0 or cnt0 == len(s) or cnt1 == len(s):
        print(-1)
    else:
        d = abs(cnt1 - cnt0)
        if d == 0:
            print(0)
        else:
            print(d // 2)
