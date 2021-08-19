def max_number(n):
    digits = str(n)
    digits_arr = []
    largest = ''
    for i in range(len(digits)):
        digits_arr.append(int(digits[i]))
    sorted_arr = sorted(digits_arr)[::-1]
    for j in range(len(sorted_arr)):
        largest += str(sorted_arr[j])
    return int(largest)
