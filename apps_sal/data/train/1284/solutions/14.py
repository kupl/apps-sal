for T in range(int(input())):
 N = int(input())
 A = sorted(list(map(int,input().split())))
 a = N // 4
 b = a + a
 c = b + a
 if A[a] == A[a-1] or A[b] == A[b-1] or A[c] == A[c-1]:
  print(-1)
 else:
  print(A[a],A[b],A[c])
