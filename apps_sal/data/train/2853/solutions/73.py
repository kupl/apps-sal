def solve(arr):
    seen = []
    return_list = []
    for number in arr[::-1]:
        if number not in seen:
            seen.append(number)
            return_list.append(number)
    return return_list[::-1]
