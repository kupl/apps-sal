def productFib(prod):
    num = 1
    prev = 0
    while prev * num < prod:
        temp = num + prev
        prev = num
        num = temp
    return [prev, num, prev * num == prod]
