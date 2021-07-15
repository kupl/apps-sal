def solve(arr):
    lst = []
    for string in arr:
        counter = 0
        for index, letter in enumerate(string):
            if index + 1 == ord(letter.upper()) - 16 * 4:
                counter += 1
        lst.append(counter)
    return lst
