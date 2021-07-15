n = int(input())

if n == 1:
    print(1)
else:
    chunkn = 2
    ans = (n + 1) // 2 + 2
    for curChunkn in range(3, n + 1):
        chunk = n // curChunkn
        curAns = chunk + curChunkn
        if n % curChunkn > 0:
            curAns += 1
        
        if curAns > ans:
            break
        ans = curAns
        chunkn = curChunkn
    
    lim = n
    left = n % chunkn
    for i in range(chunkn):
        start = lim - (n // chunkn) + 1
        if left > 0:
            left -= 1
            start -=1
        for j in range(start, lim + 1):
            print(j, end=' ')
        lim = start - 1
        
