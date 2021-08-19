# cook your dish here
t = int(input())
for i in range(t):
    n = input()
    l = len(n)
    if(len(n) < 4):
        print("NO")
    elif(n[l - 1] == '0' and n[l - 2] == '0' and n[l - 3] == '0' and n[l - 4] == '1'):
        print("YES")
    else:
        print("NO")
