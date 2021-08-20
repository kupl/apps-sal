N = int(input())
min_arr = [0 for _ in range(N)]
for i in range(N):
    arr_i = [n - 1 for n in map(int, input().split())]
    for j in range(N):
        if i == j:
            continue
        min_arr[i] = max(arr_i[j], min_arr[i])
        min_arr[j] = max(arr_i[j], min_arr[j])
assign = [0 for _ in range(N)]
blah = [(min_arr[i], i) for i in range(N)]
blah.sort()
for i in range(N):
    assign[blah[i][1]] = i + 1
print(' '.join(map(str, assign)))
