def pay_cheese(arr):
    (a, b) = divmod(sum(arr), 100)
    return 'L' + str(int((a + (b > 0)) * 35))
