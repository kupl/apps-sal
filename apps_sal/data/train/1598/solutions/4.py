#Help the teacher
for _ in range(int(input())):
 n = int(input())
 list1 = []
 for i in range(n):
  list1.append(list(map(str,input().split())))
 sums = 0
 for i in list1:
  sums += int(i[2])
 avg = sums/n
 ans = []
 for i in list1:
  if(avg>int(i[2])):
   ans.append(i)
 ans.sort(key = lambda ans: int(ans[2]))
 for i in ans:
  print(*i)
