# cook your dish here
import math
T = int(input())
for _ in range(T):
 N, A, K = list(map(int, input().split(" ")))
 total = (N-2) * 180
 
 # 360 = 60 + (1+2+3)*diff + 3*60
 # 360 = 240 + 6*diff
 # 120 = 6*diff
 # 120 / 6 = diff
 
 # K: 60 + (K-1) * diffT / diffN = (60*diffN+(K-1)*diffT) / diffN
 
 diffT = total - N*A
 diffN = sum(range(1,N))
 r = (A*diffN+(K-1)*diffT)
 
 d = math.gcd(r, diffN)
 while d > 1:
  r//=d
  diffN//=d
  d = math.gcd(r, diffN)
 print(r, diffN)

