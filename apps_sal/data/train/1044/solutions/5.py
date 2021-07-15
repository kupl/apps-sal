# cook your dish here
n=int(input())
for _ in range(n):
    a=int(input())
    sum=0
    while a>0:
        rem=a%10
        sum=sum+rem
        a=a//10
    print(sum)

