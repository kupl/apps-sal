def max_number(n):
    num = [x for x in str(n)]
    swap = True
    while swap:
        swap = False
        for i in range(len(num) - 1):
            if num[i] < num[i + 1]:
                num[i], num[i + 1] = num[i + 1], num[i]
                swap = True
    output = ''
    return int(output.join(num))
