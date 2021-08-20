t = int(input())
for _ in range(t):
    n = int(input())
    s = input()
    c = abs(s.count('L') - s.count('R')) + abs(s.count('U') - s.count('D'))
    print(n - c)
