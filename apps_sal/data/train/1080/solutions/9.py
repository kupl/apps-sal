t = int(input())
while(t):
    x = input()
    a = len(x)
    if a == 1:
        print("NO")

    elif a == 2:
        if x[0] == x[1]:
            print("NO")
        else:
            print("YES")
    else:
        if x[0] == x[1]:
            print("NO")
        else:
            for j in range(a - 2):
                if x[j] == x[j + 2]:
                    if j == a - 3:
                        print("YES")
                        break
                else:
                    print("NO")
                    break
    t -= 1
