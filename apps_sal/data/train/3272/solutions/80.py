def find_average(nums):
    # your code here
    if nums == []:  # or len(nums)==0:
        return 0
    else:
        b = len(nums)
        print(b)
        a = sum(nums)
        c = a / b
        return c
