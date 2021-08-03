# cook your dish here
n, q = map(int, input().split(' '))

n_bonacci = list(map(int, input().split(' ')))
arr = []
xor = 0
for val in n_bonacci:
    xor = xor ^ val
    arr.append(xor)

for query in range(q):
    s = int(input())

    if s % (n + 1) == 0:
        print(0)
    else:
        print(arr[s % (n + 1) - 1])
