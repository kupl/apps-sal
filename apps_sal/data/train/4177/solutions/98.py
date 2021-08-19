def men_from_boys(arr):
    even_arr = []
    odd_arr = []
    for number in arr:
        if number % 2 == 0:
            even_arr.append(number)
        else:
            odd_arr.append(number)
    even_arr.sort()
    odd_arr.sort()
    odd_arr.reverse()
    result = []
    for number in even_arr:
        if number not in result:
            result.append(number)
    for number in odd_arr:
        if number not in result:
            result.append(number)
    return result
