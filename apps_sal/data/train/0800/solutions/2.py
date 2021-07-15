# cook your dish here
try:
    n=int(input())
    num = list(map(int, input().split()[:n]))
    m1=max(num)
    m2=min(num)
    print(m1,m2)

except:
    pass
