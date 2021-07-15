for t in range(int(input())):
 n, k, e, m = map(int,input().split())
 stud = n-k-1
 sum_list = []
 for i in range(n-1):
  l = list(map(int, input().split()))
  sum_list.append(sum(l))
 score = list(map(int,input().split()))
 sum_sergey = sum(score)
 sum_list.sort()
 x = sum_list[stud] + 1 - sum_sergey
 if x<m and x>0:
  print(x)
 elif x<=0:
  print(0)
 else:
  print("Impossible")
