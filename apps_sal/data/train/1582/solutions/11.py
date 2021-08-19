# cook your dish here
n = int(input())
st = input()
cnt = 0
for i in range(len(st) - 1):
    if st[i] == st[i + 1]:
        cnt += 1
print(cnt)
