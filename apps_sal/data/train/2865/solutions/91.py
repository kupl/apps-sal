def solution(string):
    reverse = ''
    for i in range(len(string)):

        # this won't work because strings are immutable
        # reverse[i]=string[-i]

        # however, you can assign each character to a string
        reverse = reverse + string[-i - 1]

    return reverse
