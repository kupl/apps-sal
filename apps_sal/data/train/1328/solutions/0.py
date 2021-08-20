for _ in range(0, int(input())):
    n = input().strip()
    x = n.count('4')
    y = n.count('7')
    print(len(n) - x - y)
