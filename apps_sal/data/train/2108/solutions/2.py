a,b=input().split()
print(a,b)
for i in range(int(input())):
    c,d=input().split()
    if a==c:
        a=d
    elif b==c:
        b=d
    print(a,b)

