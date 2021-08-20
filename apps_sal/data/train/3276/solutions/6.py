def missing(nums, stri):
    nums = sorted(nums)
    stri = stri.replace(' ', '')
    return ''.join([stri[i].lower() for i in nums]) if max(nums) < len(stri) else 'No mission today'
