a = input()
res = 0
cur = 0
for i in reversed(a):
    if (i == 'b'):
        cur+=1
    else:
        res+=cur
        res%=1000000007
        cur= cur*2%1000000007
print(res)
