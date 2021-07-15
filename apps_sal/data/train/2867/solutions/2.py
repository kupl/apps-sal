def fix_progression(arr):
    best = len(arr)
    s = sum(arr) / len(arr)
    for start in range(len(arr)-1):
        for idx in range(start+1, len(arr)):
            count = 0
            d = (arr[idx] - arr[start]) // (idx - start)
            for i in range(0, start):
                if arr[i] != arr[start] - d*(start-i):
                    count += 1
            for i in range(start+1, len(arr)):
                if arr[i] != arr[start] + d*(i-start):
                    count += 1
            best = min(best, count)
    return best

