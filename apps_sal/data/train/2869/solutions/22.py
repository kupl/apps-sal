def distinct(num):
    uni = []
    for n in num:
        if n not in uni:
            uni.append(n)
    return uni
