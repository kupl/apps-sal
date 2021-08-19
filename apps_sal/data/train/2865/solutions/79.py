def solution(string):
    reverse = ''
    letter_index = len(string) - 1
    for x in range(len(string)):
        reverse = reverse + string[letter_index]
        letter_index -= 1
    return reverse
