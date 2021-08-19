N = int(input())
sum = 0
min = 10 ** 9 + 1
for i in range(N):
    (A, B) = map(int, input().split())
    if A > B and min > B:
        min = B
    sum += A
if min == 10 ** 9 + 1:
    print(0)
else:
    print(sum - min)
