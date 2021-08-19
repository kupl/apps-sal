n = input()
cnt = 0
x = n[0]
for i in range(len(n)):
    if n[i] != x:
        cnt += 1
        x = n[i]
if n[-1] == '1':
    print(cnt + 1)
else:
    print(cnt)
