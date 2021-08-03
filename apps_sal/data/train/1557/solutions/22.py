t = int(input())
for i in range(t):
    n = int(input())
    s = input()
    r = input()
    if(s.count("1") == r.count("1")):
        print("YES")
    else:
        print("NO")
