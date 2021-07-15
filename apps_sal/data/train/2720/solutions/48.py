def solution(digits):
    nw_lst=[]
    for i in range(len(digits)-4):
        nums = int(digits[i:i+5])
        nw_lst.append(nums)
    return max(nw_lst);
