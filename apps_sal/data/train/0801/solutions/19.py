for i in range(int(input())):
 n = int(input())
 a = [int(i) for i in input().split()]
 b = [int(i) for i in input().split()]
 A = {}
 B = {}
 x = 0
 Min = 10**9
 for i in a:
  if i in list(A.keys()):
   A[i] += 1
  else:
   A[i] = 1

  if i < Min:
   Min = i
  x = x ^ i

 for i in b:
  if i in list(B.keys()):
   B[i] += 1
  else:
   B[i] = 1
  if i < Min:
   Min = i
  x = x ^ i

 if x != 0:
  print('-1')
  continue

 a = []
 b = []
 for i in list(A.keys()):
  if i in list(B.keys()) and A[i] == B[i]:
   pass
  else:
   if i in list(B.keys()):
    if A[i] > B[i]:
     for j in range((A[i]-B[i])//2):
      a.append(i)
   else:
    for j in range(A[i]//2):
     a.append(i)

 for i in list(B.keys()):
  if i in list(A.keys()) and A[i] == B[i]:
   pass
  else:
   if i in list(A.keys()):
    if B[i] > A[i]:
     for j in range((B[i]-A[i])//2):
      b.append(i)
   else:
    for j in range(B[i]//2):
     b.append(i)

 a = sorted(a)
 b = sorted(b)
 j = -1
 if len(a) != len(b):
  print('-1')
  continue
 cost = 0
 for i in range(len(a)):
  if min(a[i], b[j]) < 2*Min:
   cost += min(a[i], b[j])

  else:
   cost += 2*Min

  j -= 1
 print(cost)

