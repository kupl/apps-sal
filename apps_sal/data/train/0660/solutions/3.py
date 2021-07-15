# cook your dish here
a=[1]
fact=[1]
for i in range(1,15):
    fact.append(fact[i-1]*i)
for i in range(int(input())):
    n=int(input())
    if n in [1,2,1,145,40585]:
        print(1)
    else:
        print(0)

