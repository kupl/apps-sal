def multiple_of_index(arr):
    output = []
    count = 0
    for num in arr:
        if count != 0:
            if not num % count:
                output.append(num)
        count += 1
    return output
