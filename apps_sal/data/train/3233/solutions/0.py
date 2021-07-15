def robot_transfer(matrix, k):
    c = 0
    for l, i in enumerate(matrix):
        for o, j in enumerate(i):
            x, y = j.split(",")
            current,count,new = [l, o],0,[]
            while count < k and current != new:
                new = [int(x), int(y)] ; x, y = matrix[int(x)][int(y)].split(",") ; count += 1
            if current == new and count == k : c += 1
    return c 
