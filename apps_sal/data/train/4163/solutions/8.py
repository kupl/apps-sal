def is_centered(arr,n):
    for i in range(len(arr)):
        for j in range(len(arr)+1):
            if j>i:
                if sum(arr[i:j]) == n and i == len(arr)-j:
                    return True
    return True if n==0 and arr!=arr[::-1] else False
