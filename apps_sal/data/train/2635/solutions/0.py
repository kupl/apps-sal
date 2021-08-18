s = input()
ss = input()
cnt = 0
len_s = len(s)
len_ss = len(ss)
for i in range(0, len_s):
    tmp = s[i:i + len_ss]
    if(tmp == ss):
        cnt = cnt + 1
print(cnt)
