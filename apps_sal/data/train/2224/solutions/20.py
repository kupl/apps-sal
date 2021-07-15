n = int(input())
s1 = input()
s2 = input()
smth = dict()
smth['01'] = 0
smth['00'] = 0
smth['10'] = 0
smth['11'] = 0
ans = 0
for i in range(n):
    smth[s1[i] + s2[i]] += 1
for i in range(n):
    if s1[i] == '0':
        if s2[i] == '0':
            ans += smth['10']
            ans += smth['11']
        else:
            ans += smth['10']
print(ans)
