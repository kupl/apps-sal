def password(n):
    num=str(n)
    hack=""
    for i in num:
        hack=hack+str(int(i)-2)
    print(hack)
    
    
for _ in range(int(input())):
    n=int(input())
    password(n)
