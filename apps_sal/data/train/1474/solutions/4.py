for t in range(eval(input())):
 N = eval(input())
 A = input().split(' ')
 B = eval(input())
 count = [0 for x in range(N)]
 
 for i in range(N):
  A[i] = list(A[i])
  for j in range(len(A[i])):
   if A[i][j] == str(B):
    count[i] += 1
  A[i] = ''.join(A[i])
 print(A[count.index(max(count))])

