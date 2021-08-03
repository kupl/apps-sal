import string


def solve(arr):
    alphabet = string.ascii_lowercase
    result = []
    for i in range(len(arr)):
        part_result = 0
        test_word = arr[i].lower()
        for j in range(len(test_word)):
            if j >= len(alphabet):
                continue
            if test_word[j] == alphabet[j]:
                part_result += 1
        result.append(part_result)
    return result
