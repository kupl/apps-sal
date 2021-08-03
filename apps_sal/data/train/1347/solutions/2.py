n, m = list(map(int, input().split()))
S = list(map(int, input().split()))
special = []
nonspecial = []
for i in range(m):
    A = input().split()
    if int(A[0]) in S:
        special.append(A)
    else:
        nonspecial.append(A)

special.sort(key=lambda x: int(x[1]), reverse=True)
nonspecial.sort(key=lambda x: int(x[1]), reverse=True)

for i in special:
    print(i[2])
for i in nonspecial:
    print(i[2])
