t = int(input())

for i in range(t):
 w,k = map(int,input().split())
 l = [int(x) for x in input().split()]
 l.sort()
 sum_w = sum(l)
 s1 = 0
 s2 = 0
 start = 0
 end = len(l) - 1
 while k > 0:
  s1 += l[start]
  s2 += l[end]
  start += 1
  end -= 1
  k -= 1
 print(max(abs(s1 - (sum_w - s1)) , abs(s2 - (sum_w - s2))))
