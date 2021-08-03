def balanced_num(num):
    str_num = str(num)
    len_num = len(str_num)
    if len_num % 2 != 0:
        nums = str_num[0:int(len_num / 2)], str_num[int(len_num / 2 + 1):len_num]
        print((nums, sum(list(map(int, nums[0]))), sum(list(map(int, nums[1])))))
        return "Balanced" if sum(list(map(int, nums[0]))) == sum(list(map(int, nums[1]))) else "Not Balanced"

    else:
        nums = str_num[0:int(len_num / 2 - 1)], str_num[int(len_num / 2 + 1):len_num]
        print((nums, sum(list(map(int, nums[0]))), sum(list(map(int, nums[1])))))
        return "Balanced" if sum(list(map(int, nums[0]))) == sum(list(map(int, nums[1]))) else "Not Balanced"
