n=int(input())
modulo=15746
num=[1,1]
for i in range(2,n+1):
    num.append((num[i-1]+num[i-2])%modulo)
print(num[n])
