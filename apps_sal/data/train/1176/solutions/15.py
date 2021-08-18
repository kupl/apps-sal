t = int(input())
for i in range(t):
    s = input()
    if len(s) > 3:
        if s[-1] == '0' and s[-2] == '0' and s[-3] == '0' and s[-4] == '1':
            print("YES")
        else:
            print("NO")
    else:
        print("NO")
