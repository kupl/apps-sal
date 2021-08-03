def first_non_repeating_letter(string):
    low = string.lower()
    a = [ele for ele in dict.fromkeys(low) if low.count(ele) == 1]
    return string[low.index(a[0])] if a and string else ''
