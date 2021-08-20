def two_sort(array):
    final = ''
    word = list(sorted(array)[0])
    for i in range(len(word)):
        if i != len(word) - 1:
            final += word[i] + '***'
        else:
            final += word[i]
    return final
