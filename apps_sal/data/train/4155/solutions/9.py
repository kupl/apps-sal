def solve(a, b):
    count = 0
    for num in range(a, b):
        num = str(num)
        if num == num.translate(str.maketrans('1234567890', '1xxxx9x860'))[::-1]:
            count += 1
    return count
