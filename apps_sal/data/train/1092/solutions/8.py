for i in range(int(input())):
 n, k, e, m = list(map(int,input().split()))
 stu = n-k-1
 sum_list = []
 for i in range(n-1):
  l = list(map(int, input().split()))
  sum_list.append(sum(l))
 score = list(map(int,input().split()))
 sum_ser = sum(score)
 sum_list.sort()
 x = max(sum_list[stu] + 1 - sum_ser,0)
 if x<m:
  print(x)
 else:
  print("Impossible")

