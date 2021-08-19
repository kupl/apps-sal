def ret_sum(arr, k, x):
    s = 0
    for i in arr:
        s += abs((x - i) ** k)
    return s


(n, k) = list(map(int, input().split()))
arr = list(map(int, input().split()))
(start, end) = (min(arr), max(arr))
hash_arr = {}
flag = 0
while start <= end and flag == 0:
    mid = (start + end) // 2
    mid_prev = mid - 1
    mid_next = mid + 1
    if mid not in hash_arr:
        hash_arr[mid] = ret_sum(arr, k, mid)
    if mid_next not in hash_arr:
        hash_arr[mid_prev] = ret_sum(arr, k, mid_prev)
    if mid_next not in hash_arr:
        hash_arr[mid_next] = ret_sum(arr, k, mid_next)
    if hash_arr[mid_prev] > hash_arr[mid] and hash_arr[mid_next] > hash_arr[mid]:
        print(mid)
        flag = 1
        break
    elif hash_arr[mid_next] < hash_arr[mid]:
        start = mid
    else:
        end = mid
