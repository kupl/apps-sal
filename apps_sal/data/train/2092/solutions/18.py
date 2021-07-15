n = int(input())
home = input()
cnt = 0
for i in range(n):
    s = input()
    s.split('->')
    cnt += s.count(home)
if cnt % 2 == 0:
    print('home')
else:
    print('contest')
