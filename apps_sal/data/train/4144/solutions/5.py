def abundant(h):
    for i in range(h+1)[::-1]:
        sum = 0
        for j in range(1,i):
            if i%j==0:
                sum += j
        if sum>h:
            return [[i],[sum-i]]
