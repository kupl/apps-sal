def fold_cube(nums):
    stack = [nums[0]]
    for _ in range(6):
        for i in range(len(stack)):
            if ((stack[i]-1) % 5 > 0) and ((stack[i] - 1) in nums) and ((stack[i] - 1) not in stack):
                stack.append(stack[i] - 1)
            if ((stack[i]-1) % 5 < 4) and ((stack[i] + 1) in nums) and ((stack[i] + 1) not in stack):
                stack.append(stack[i] + 1)
            if ((stack[i]-1) > 5) and ((stack[i] - 5) in nums) and ((stack[i] - 5) not in stack):
                stack.append(stack[i] - 5)
            if ((stack[i]-1) < 21) and ((stack[i] + 5) in nums) and ((stack[i] + 5) not in stack):
                stack.append(stack[i] + 5)
    print(stack)
    print(nums)
    
    
    if len(stack) != 6:
        return False
    cols = []
    for n in stack:
        if ((n-1) % 5) not in cols:
            cols.append((n-1) % 5)
    rows = []
    for n in stack:
        if (int((n-1) / 5)) not in rows:
            rows.append(int((n-1) / 5))
#     print()
#     print(rows)
#     print()
#     print(cols)
    if len(rows) + len(cols) != 7:
        return False
    if len(rows) == 2:
        if (sum(rows)+1)/2*5+ sum(cols)/5+1 not in stack or (sum(rows)-1)/2*5+ sum(cols)/5+1 not in stack:
            return False
    if len(rows) == 3:
        if sum(rows)/3*5+(sum(cols)+2)/4+1 not in stack or sum(rows)/3*5+(sum(cols)-2)/4+1 not in stack:
            print((3))
            return False
    if len(rows) == 4:
        if (sum(rows)+2)/4*5+sum(cols)/3+1 not in stack or (sum(rows)-2)/4*5+sum(cols)/3+1 not in stack:
            print((4))
            return False
    if len(rows) == 5:
        if sum(rows)+ (sum(cols)+1)/2+1 not in stack or sum(rows)+ (sum(cols)-1)/2+1 not in stack:
            print((5))
            return False
    if len(rows) == 2:
        if sum(stack)%30 != 3:
            return False
    if len(rows) == 5:
        if sum(stack)%6 != 3:
            return False
    print(True)
    return True
            
        
        
    

