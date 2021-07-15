def solve(arr): 
    output = []
    
    for x in arr[::-1]:
        if x in output:
            continue
        else:
            output.append(x)
    return output[::-1]
