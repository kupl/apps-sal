def reverse_number(n):
    print(n)
    if n >= 0:
        return int(str(n)[::-1])
        # print(int(str(n)[::-1]))
    else:
        return -int(str(n)[:0:-1])
        # print(-int(str(n)[:0:-1]))
