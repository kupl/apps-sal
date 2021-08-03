def triple_double(num1, num2):
    num1 = str(num1)
    num2 = str(num2)
    nums = ['1', '0', '2', '3', '4', '5', '6', '7', '8', '9', '0']
    for i in nums:
        if i * 3 in num1 and i * 2 in num2:
            return 1
    return 0
