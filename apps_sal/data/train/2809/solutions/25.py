def digitize(n):
    output = []
    for digit in str(n):
        output.append(int(digit))
    return(output[::-1])
