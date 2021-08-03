# Largest Numeric Palindrome
printit = False


def prefilter(available):
    ones = None
    for _ in range(available.count(0)):
        available.remove(0)
    if len(available) == 1:
        available.append(0)
    for _ in range(available.count(1)):
        available.remove(1)
        ones = True
    if len(available) >= 1 and ones:
        available.extend([1])
    elif len(available) == 1 and ones:
        available.extend([1])
    elif len(available) == 0 and ones:
        available.extend([1, 1])
    else:
        available.extend([0, 0])


def comb(available, used):
    if len(available) == 0:
        pass
    else:
        head = available.pop()
        used.append(head)
        if len(used) >= 2:
            yield(list(used))
        for x in comb(available[:], used[:]):
            yield x
        used.pop()
        for x in comb(available[:], used[:]):
            yield x


def numeric_palindrome(*args):
    lst = [*args]
    prefilter(lst)
    lst = [x for x in comb(lst, [])]
    if printit:
        print('sorted:', sorted([sorted(x) for x in lst]))
    if lst == []:
        return 0
    if printit:
        print(lst)
    products = []
    for nums in lst:
        result = 1
        for num in nums:
            result *= num
        products.append(str(result))
    products = [str(x) for x in products]
    if printit:
        print(products)
    lsts = [sorted([int(char) for char in product], reverse=True) for product in products]
    if printit:
        print(lsts)
    palindromes = []
    pal_ind = 0
    for nums in lsts:
        sel_nums = []
        if printit:
            print(sel_nums)
        odd_added = False
        for num in sorted(list(set(nums)), reverse=True):
            num_count = nums.count(num)
            if num_count % 2 == 0:
                for i in range(num_count):
                    sel_nums.append(num)
            elif num_count % 2 == 1 and not odd_added:
                for i in range(num_count):
                    sel_nums.append(num)
                    odd_added = True
            else:
                for i in range(num_count - 1):
                    sel_nums.append(num)
                    odd_added = True
        if printit:
            print('sel_nums:', sel_nums)
        i = 0
        while len(sel_nums) > 0:
            if sel_nums.count(sel_nums[0]) == 1:
                sel_nums.append(sel_nums.pop(0))
            if len(sel_nums) > 1 and i == 0:
                palindromes.insert(pal_ind, [])
                palindromes[pal_ind].insert(0, str(sel_nums.pop(0)))
                palindromes[pal_ind].insert(1, str(sel_nums.pop(0)))
                if printit:
                    print('first branch, i:', str(i), palindromes[pal_ind])
                i += 1
                continue
            elif len(sel_nums) == 1 and i == 0:
                palindromes.insert(pal_ind, list(str(sel_nums.pop(0))))
                if printit:
                    print('second branch, i:', str(i), palindromes[pal_ind])
                i += 1
                continue
            elif len(sel_nums) >= 2:
                palindromes[pal_ind].insert(i, str(sel_nums.pop(0)))
                palindromes[pal_ind].insert(-i, str(sel_nums.pop(0)))
                if printit:
                    print('third branch, i:', str(i), palindromes[pal_ind])
                i += 1
                continue
            elif len(sel_nums) == 1:
                palindromes[pal_ind].insert(i, str(sel_nums.pop()))
                if printit:
                    print('forth branch, i:', str(i), palindromes[pal_ind])
                i += 1
                continue
        if printit:
            print('building:', palindromes[pal_ind])
            print(str(i))
        pal_ind += 1
    palindromes = [int(''.join(x)) for x in palindromes]
    while str(max(palindromes))[-1] == '0' and len(str(max(palindromes))) > 1:
        max_num = max(palindromes)
        new_num = str(max_num).strip('0')
        palindromes.remove(max_num)
        palindromes.append(int(new_num))
    return max(palindromes)
