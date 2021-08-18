for _ in range(int(input())):
    n = int(input())
    a = input()
    b = input()
    if a.count('1') == b.count('1'):
        print("YES")
    else:
        print("NO")
