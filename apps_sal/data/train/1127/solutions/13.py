# cook your dish here
for _ in range(int(input())):
    n=[i for i in input().split()]
    c=""
    for i in n:
        if i==n[-1]:
           c+=i.capitalize()
        else:
            v=i.capitalize()
            c+=v[0]+'. '
            
    print(c)
