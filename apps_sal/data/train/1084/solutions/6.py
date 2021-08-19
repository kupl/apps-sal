# cook your dish here
l = input()
cnt = 0
n = len(l)
for i in range(n - 1):
    if(l[i] != l[i + 1]):
        cnt += 1
if(l[-1] == '1'):
    cnt += 1
print(cnt)
