def even_magic(n):
    arr = [];
    for i in range(0, n):
        arr.append([])
        for j in range(0, n):
            if i%4==j%4 or i%4+j%4 == 3:
                arr[i].append(n*n-i*n-j)
            else:
                arr[i].append(i*n+j+1)
    return arr
