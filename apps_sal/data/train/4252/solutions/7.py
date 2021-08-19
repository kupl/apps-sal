def merge_arrays(first, second):
    bound = 0
    first = list(dict.fromkeys(first))
    second = list(dict.fromkeys(second))
    for indexB in range(len(second)):
        for indexA in range(bound, len(first)):
            if second[indexB] in first:
                break
            elif second[indexB] < first[indexA]:
                first.insert(indexA, second[indexB])
                bound += 1
                break
            elif indexA == len(first) - 1 and second[indexB] > first[indexA]:
                first.insert(indexA + 1, second[indexB])
    return first
