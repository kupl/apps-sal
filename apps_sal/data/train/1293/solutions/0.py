def update_B(B, query):
 p, R = query
 for i in range(len(R)):
  B[p][i] = R[i]
  B[i][p] = R[i]

def get_A(B):
 N = len(B)
 A = [0] * N
 i = 0
 for j in range(N):
  if B[0][j] != 0:
   i = j
   A[i] = -B[0][i]
   break

 for j in range(i + 1, N):
  if abs(A[i] - B[0][j]) == B[i][j]:
   A[j] = B[0][j]
  else:
   A[j] = -B[0][j]

 return A

def print_list(A):
 print(' '.join([str(a) for a in get_A(B)]))


N, Q = [int(x) for x in input().rstrip().split()]
B = []
for i in range(N):
 B += [[int(x) for x in input().rstrip().split()]]
queries = []
for i in range(Q):
 p = int(input()) - 1
 arr = input().rstrip().split()
 queries += [(p, [int(x) for x in arr])]

print_list(get_A(B))
for q in queries:
 update_B(B, q)
 print_list(' '.join([str(a) for a in get_A(B)]))

