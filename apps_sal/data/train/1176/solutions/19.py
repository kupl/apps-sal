t = int(input())
for _ in range(t):
    n = input()
    if len(n) < 4:
        print("NO")
    else:
        if n[-1] == '0' and n[-2] == '0' and n[-3] == '0' and n[-4] == '1':
            print("YES")
        else:
            print("NO")
