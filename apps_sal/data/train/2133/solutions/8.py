n = int(input())
A = []
for q in range(0, 7):
    A.append(0)
c = 0
while 1:
    if c == n:
        break
    x = input()
    b = 0
    for i in range(0, 7):
        if x[i] == '1':
            A[i] = A[i] + 1
    c = c + 1
max = 0
for d in range(0, 7):
    if A[d] > max:
        max = A[d]
print(max)
