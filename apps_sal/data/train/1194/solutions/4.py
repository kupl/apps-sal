for _ in range(int(input())):
 n = int(input())
 s = list(str(input()))
 c1 = abs(s.count('U') - s.count('D')) + abs(s.count('R') - s.count('L'))
 print(n-c1)
