N = eval(input())
dict1 = {}
list1 = list(map(int, input().split()))

for i in list1:
 dict1[i] = 1

for i in range(1,N + 1):
 if i not in dict1:
  print(i, end=' ') 
