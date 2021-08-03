for _ in range(int(input())):
    n = input().strip()
    print(len(n) - (n.count('4') + n.count('7')))
