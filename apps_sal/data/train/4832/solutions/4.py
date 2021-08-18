def all_non_consecutive(arr):
    start = 0
    answer = []
    for number in arr:
        if start == 0:
            current = number
            start = 1
            continue
        elif number != current + 1:
            format = {'i': arr.index(number), 'n': number}
            answer.append(format)
        current = number
    return answer
