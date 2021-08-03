'''
Created on ١٢‏/١٢‏/٢٠١٤

@author: mohamed265
'''
'''
s = input()
n = len(s)
slon = ""
for i in range(1, n):
    if s[i] == '0' and s[i - 1] != '0':
        t = s[0:i] + s[i + 1:n]
        slon = max(slon, t)
if len(slon) != n - 1:
    slon = s[1:]
print(slon)

s = input()
n = len(s)
slon = ""
k = temp = 0
for i in range(1, n):
    if s[i] == '0':
        t = s[0:i] + s[i + 1:n]
        k = int(t, 2)
        print(t , k)
        if k > temp:
            temp = k
            slon = t
if len(slon) != n-1:
    slon = s[1:]
print(slon)
'''
s = input()
temp = s.find('0')
print(s[1:]) if temp == -1 else print(s[0:temp] + s[temp + 1:])
