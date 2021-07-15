import sys
for _ in range(int(sys.stdin.readline())):
 a=list(map(str,sys.stdin.readline().strip().split()))[0]
 print(a.strip('0')[::-1])
