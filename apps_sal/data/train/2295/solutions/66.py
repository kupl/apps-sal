n = int(input())
(A, B) = map(list, zip(*[map(int, input().split()) for i in range(n)]))
if A == B:
    print(0)
else:
    print(sum(A) - min([B[i] for i in range(n) if A[i] > B[i]]))
