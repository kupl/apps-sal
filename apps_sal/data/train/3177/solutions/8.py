def check_array(array):
    if len(array) > 1:
        mid = int(len(array) / 2)
        if len(array) % 2 == 0:
            mid = int(len(array) / 2)
            first = array[:mid]
            second = array[mid:]
        else:
            first = array[:mid]
            second = array[mid + 1:]
        second.reverse()
        if first == second:
            str_arr = ''
            for i in array:
                str_arr += str(i)
            pal = int(str_arr)
            pal2 = str(pal)
            if pal2 == str_arr:
                return pal


def palindrome(num):
    if isinstance(num, int) != True or num < 0:
        return 'Not valid'
    if num < 10:
        return 'No palindromes found'
    array = []
    for i in str(num):
        array.append(int(i))
    array_list = []
    for i in range(len(array)):
        part = array[i:]
        p = check_array(part)
        if p != None and p != 0:
            array_list.append(p)
        for j in range(len(part)):
            back = part[:-j]
            b = check_array(back)
            if b != None and b != 0:
                array_list.append(b)
    array_set = set(array_list)
    result = list(array_set)
    result.sort()
    if len(result) == 0:
        return 'No palindromes found'
    else:
        return result
