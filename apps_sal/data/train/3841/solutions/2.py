from itertools import permutations


def get_words(hash_of_letters):
    string = ''
    for i in hash_of_letters:
        string += ''.join(hash_of_letters[i] * i)
    answer = set(permutations(string))
    answer = sorted(answer)
    for i in range(len(answer)):
        answer[i] = ''.join(answer[i])
    return answer
