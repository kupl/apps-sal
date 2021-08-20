def balanced_num(number):
    l = len(str(number))
    List = list(str(number))
    if l == 1 or l == 2:
        return 'Balanced'
    else:
        sum1 = sum2 = 0
        if l % 2 == 0:
            for i in range(0, l // 2 - 1):
                j = -i - 1
                sum1 += int(List[i])
                sum2 += int(List[j])
        else:
            for i in range(0, l // 2):
                j = -i - 1
                sum1 += int(List[i])
                sum2 += int(List[j])
    return 'Balanced' if sum1 == sum2 else 'Not Balanced'
