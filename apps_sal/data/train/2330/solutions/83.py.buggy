s = input()
n = len(s)

if s[n - 1] == '1' or s[0] == '0':
    print(-1)
    return

for i in range(n):
    if s[i] != s[n - i - 2]:
        print(-1)
        return

cur_s = 2
cur_p = 2
print(1, 2)
for i in range(n - 2):
    if s[i + 1] == '1':
        print(cur_s + 1, cur_p)
        cur_p = cur_s + 1
    else:
        print(cur_s + 1, cur_p)
    cur_s += 1
