n = int(input())
s = input()
ss = []
cnt = 0
for i in range(n):
    t = input()
    t = t.split('->')
    cnt += t[1] == s
    ss.append((t))
if(cnt == n//2 and n%2 == 0):
    print('home')
else:
    print('contest')
