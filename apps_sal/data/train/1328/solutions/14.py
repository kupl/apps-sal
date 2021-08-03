for _ in range(int(input())):
    n = input().strip()
    seven, four = n.count('7'), n.count('4')
    x = seven + four
    print(len(n) - x)
