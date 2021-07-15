from sys import stdin
import heapq
MOD = pow(10, 9) + 7
n=int(stdin.readline())
a=[]
for i in range(n):
    x=stdin.readline().split()
    if x[0]=='ADD':
        a.append((0,int(x[1])))
    else:
        a.append((1,int(x[1])))
next_accept=[-1]*n
accept = -1
for i in range(n-1, -1, -1):
    if a[i][0]== 1:
        accept=i
    next_accept[i] = accept
top = []
bottom = []
buysell_n = 0
last_n=0
invalid = False
for i in range(n):
    if a[i][0] == 0:
        if next_accept[i] != -1:
            if a[i][1] > a[next_accept[i]][1]:
                heapq.heappush(top, a[i][1])
            elif a[i][1] < a[next_accept[i]][1]:
                heapq.heappush(bottom, -a[i][1])
        elif (len(top) == 0 or a[i][1] < top[0]) and (len(bottom) == 0 or a[i][1] > -bottom[0]):
                last_n += 1
    else:
        if len(top) > 0 and a[i][1] == top[0]:
            heapq.heappop(top)
        elif len(bottom) > 0 and a[i][1] == -bottom[0]:
            heapq.heappop(bottom)
        else:
            if len(top) > 0 and a[i][1] > top[0] or len(bottom) > 0 and a[i][1] < -bottom[0]:
                invalid = True
                break
            buysell_n += 1

if invalid:
    ans = 0
else:
    ans = (pow(2, buysell_n, MOD)*(last_n+1))%MOD
print(ans)

