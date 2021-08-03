t = int(input())
d = []
for i in range(t):
    n = int(input())
    d.append(list(map(int, input().split())))

output = []
for arr in d:
    arr.sort(reverse=True)
    time = 0
    i = 0
    t = 0
    while i < len(arr):
        if t == 0:
            time += arr[i]
            t = arr[i]
        i += 1
        if i >= len(arr):
            break
        if arr[i] <= t:
            t -= arr[i]
            arr[i] = 0
        else:
            arr[i] -= t
            t = 0
    output.append(time)

for i in output:
    print(i)
