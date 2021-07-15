t = input()
p = input()
ai = list(map(int,input().split()))
n = len(ai)
ti = [[t[i],1] for i in range(n)]
for i in range(n):
    ai[i] -= 1

num2 = 1

def check(num):
    nonlocal num2
    num2 -= 1
    for i in range(num):
        ti[ai[i]][1] = num2
    num3 = 0
    for i in ti:
        if i[1] == num2:
            continue
        if i[0] == p[num3]:
            num3 += 1
            if num3 == len(p):
                return True
    return False

high = n
low = 0
mid = (high + low) // 2
while high >= low:
    if check(mid):
        low = mid + 1
    else:
        high = mid - 1
    mid = (high + low) // 2

print(mid)

