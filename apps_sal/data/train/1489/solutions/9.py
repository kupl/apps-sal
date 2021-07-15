# cook your dish here
s,k = list(map(int,input().split()))
strS = str(s)
res = ''
for i in range(0,len(strS)):
    if k>0 and strS[i] != '9':
        res += '9'
        k -= 1 
    else:
        res += strS[i]

print(int(res))

