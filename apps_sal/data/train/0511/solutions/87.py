N  = int(input())
As = list(map(int,input().split()))
array = []
B = 0
for i in range(N):
    B ^= As[i]
ans_array = []
for i in range(N):
    ans_array.append(B^As[i])
print(*ans_array)
