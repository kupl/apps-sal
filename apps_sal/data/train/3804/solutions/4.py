nums = {}

def helper():
    nums[1] = '0'
    nums[2] = '1'
    for i in range(1001):
        exp, suma = 1, 0
        for j in range(i, 0, -1):
            suma += j ** exp
            exp += 1
        nums[i] = str(suma)

def min_length_num(num_dig, ord_max):
    if not nums:
        helper()
    for num in range(1, ord_max):
        if len(nums[num]) == num_dig:
            return [True, num + 1]
    return [False, -1]
