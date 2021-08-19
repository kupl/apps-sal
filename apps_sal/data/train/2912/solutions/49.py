def find_multiples(integer, limit):
    output = [integer]
    counter = 2
    count = 1
    while output[count - 1] <= limit:
        output.append(counter * integer)
        counter += 1
        count += 1
    output.pop()
    return output
