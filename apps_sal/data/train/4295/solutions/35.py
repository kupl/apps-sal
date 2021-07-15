def sum(nums):
    ans = 0
    for num in nums:
        ans += int(num)
    return ans

def balanced_num(number):
    number = str(number)
    even = False
    middle = len(number) // 2
    if len(number) % 2 == 1:
        even = False
    else:
        even = True
    
    if not even:
        if sum(number[:middle]) == sum(number[middle + 1:]):
            return 'Balanced'
        else:
            return 'Not Balanced'
    elif even:
        if sum(number[:middle - 1]) == sum(number[middle + 1:]):
            return 'Balanced'
        else:
            return 'Not Balanced'
