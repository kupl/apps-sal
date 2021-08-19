# cook your dish here
for t in range(int(input())):
    n = int(input())
    a = list(input())
    b = list(input())
    s = []
    if len(a) == len(b):
        for i in range(0, len(a)):
            for j in range(0, len(b)):
                if a[i] == b[j]:
                    b.remove(b[j])
                    s.append(a[i])
                    break
                else:
                    pass
        if len(a) == len(s):
            print("YES")
        else:
            print("NO")

    else:
        print("YES")
