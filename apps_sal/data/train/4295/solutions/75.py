def balanced_num(number):
    nums = str(number)
    
    if len(nums) < 3:
        return 'Balanced'
    
    if len(nums) % 2 == 0:
        mid = (len(nums) - 1) // 2

        rigth_num = nums[mid:]
        left_num = nums[:mid]
        
        r_sum = [int(i) for i in list(rigth_num[2:])]
        l_sum = [int(i) for i in list(left_num)]
        
        if sum(l_sum) == sum(r_sum):
            return 'Balanced'
        else:
            return 'Not Balanced'
    else:
        mid = (len(nums)) // 2

        r_sum = [int(i) for i in list(nums[:mid])]
        l_sum = [int(i) for i in list(nums[mid+1:])]
        
        if sum(l_sum) == sum(r_sum):
            return 'Balanced'
        else:
            return 'Not Balanced'
