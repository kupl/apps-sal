def solve(arr): 
    final = []
    for number in arr[::-1]:
        if number not in final:
            final.insert(0,number)
    return final
