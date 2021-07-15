# cook your dish here
T = int(input())
for case in range(T):
 N = int(input())
 A = [int(x) for x in input().split()]
 NewA = []
 NewA.append(A[0])
 flag = False
 net = 0
 count = 0
 num = [0 for i in range(max(A)+1)]
 num[A[0]] += 1
 for i in range(1,len(A)):
  if A[i] != A[i-1] or flag:
   # print('A')
   NewA.append(A[i])
   num[A[i]] += 1
   if flag:
    # print('B')
    flag = False
  else:
   flag = True
   # print('C')
  # print(NewA,i)
 # print(NewA)
 # print(num)
 print(num.index(max(num)))



