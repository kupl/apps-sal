import string


def increment_string(strng):
    nums = ''
    righty = []
    here = ''
    for i in strng:
        print(i)
        righty.append(i)
    for i in strng[::-1]:
        if i not in string.digits:
            break
        elif i in string.digits:
            print('this is i', i)
            here = i + nums
            nums = i + nums
    if nums == '':
        righty = ''.join(righty)
        return righty + '1'
    print('first', righty)
    ok = int(nums) + 1
    ok = str(ok)
    nums = nums[:-len(ok)]
    nums = nums + ok
    print('n', nums)
    print('r', righty)
    hmmm = ''.join(righty)
    print('hr', hmmm)
    hmmm = hmmm.replace(here, nums)
    return hmmm


print(increment_string('123foo001'))
