n = int(input())
home = input()
cnt = 0
for _ in range(n):
    line = input()
    if line.startswith(home):
        cnt += 1
    elif line.endswith(home):
        cnt -= 1
if cnt == 0:
    print('home')
else:
    print('contest')
