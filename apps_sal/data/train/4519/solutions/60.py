def max_number(n):
    #your code here
    output = []

    for num in str(n):
        output.append(num)

    output = ''.join(sorted(output, reverse = True))
    
    return int(output)
