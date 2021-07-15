# cook your dish here
from sys import stdin, stdout
readline, writeline = stdin.readline, stdout.write


for _ in range(int(readline())):
 n, k, e, m = list(map(int, readline().strip().split()))
 scores = []
 for _ in range(n-1):
  scores.append(sum(list(map(int, readline().strip().split()))))
 scores.sort()
 my = sum(list(map(int, readline().strip().split())))
 ans = scores[-k]+1 - my
 print(max(0, ans) if ans <= m else "Impossible")

