def solve(arr,n):
    c,l = 0,len(arr)
    for i in range(l):
        if arr[i] == 'C':
            a = max(0,i-n)
            b = min(l-1,i+n)
            for j in range(a,b+1):
                if arr[j] == 'D':
                    arr[j] = 'd'
                    c += 1
                    break
    return c
