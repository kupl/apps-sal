def dont_give_me_five(start, end):
    nums = [str(number) for number in range(start, end + 1) if '5' not in str(number)]
    return len(nums)
