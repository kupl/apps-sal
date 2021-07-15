def solve(arr): 
    result = []
    for number in arr[::-1]:
        if number not in result:
            result.append(number)
    return result[::-1]

