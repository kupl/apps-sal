for _ in range(int(input())):
 a, b = map(int,input().split())
 team = list(list(range(1, b+1)) + [a] + list(range(b+1,a)))
 print(' '.join(map(str, team)))
