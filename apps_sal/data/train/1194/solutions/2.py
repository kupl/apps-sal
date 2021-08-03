for t in range(int(input())):
    n = int(input())
    s = str(input())
    l = abs(s.count('U') - s.count('D')) + abs(s.count('R') - s.count('L'))
    print(n - l)
