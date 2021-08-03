def reverse_letter(string):
    arr = list(string)
    arr2 = []
    for j in range(0, len(arr)):
        if arr[j].isalpha() == True:
            arr2.append(arr[j])
    return "".join(arr2[::-1])
