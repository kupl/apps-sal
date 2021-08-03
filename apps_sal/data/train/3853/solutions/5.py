def numeric_formatter(template, nums="1234567890"):
    ln = len(nums)
    lst = list(template)
    newlst = lst.copy()
    i = 0
    for idx, char in enumerate(lst):
        if char.isalpha():
            newlst[idx] = nums[i]
            i += 1
            i = i % ln
    return "".join(newlst)
