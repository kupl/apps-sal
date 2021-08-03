def solve(arr):
    answer = []
    for word in arr:
        answer.append(sum(1 for i, elem in enumerate(word.lower()) if ord(elem) - 96 == i + 1))
    return(answer)
