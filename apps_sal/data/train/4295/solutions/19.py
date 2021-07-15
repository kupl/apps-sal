def balanced_num(number):
    string_n = str(number)
    l = len(string_n)
    middle = int(l/2)
    sum_left, sum_right = 0, 0
    if l%2 == 0:
        for n in string_n[:middle-1]:
            sum_left += int(n)
        for n in string_n[middle+1:]:
            sum_right += int(n)
    else:
        for n in string_n[:middle]:
            sum_left += int(n)
        for n in string_n[middle+1:]:
            sum_right += int(n)
        
    return "Balanced" if sum_left == sum_right else "Not Balanced"
