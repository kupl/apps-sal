def find_smallest_int(arr):
    anwser = 9999999
    for a in arr:
        if a < anwser:
            anwser = a
    return anwser
