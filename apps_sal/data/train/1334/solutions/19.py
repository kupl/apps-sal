# cook your dish here
n = int(input())
array = list(map(int, input().split()))
for i in range(3, n):
    array[i] += min([array[i - 1], array[i - 2], array[i - 3]])
print(min([array[-1], array[-2], array[-3]]))
