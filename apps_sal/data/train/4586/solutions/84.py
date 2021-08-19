def tv_remote(word):
    keyboard = {'a': [1, 1], 'b': [1, 2], 'c': [1, 3], 'd': [1, 4], 'e': [1, 5], '1': [1, 6], '2': [1, 7], '3': [1, 8], 'f': [2, 1], 'g': [2, 2], 'h': [2, 3], 'i': [2, 4], 'j': [2, 5], '4': [2, 6], '5': [2, 7], '6': [2, 8], 'k': [3, 1], 'l': [3, 2], 'm': [3, 3], 'n': [3, 4], 'o': [3, 5], '7': [3, 6], '8': [3, 7], '9': [3, 8], 'p': [4, 1], 'q': [4, 2], 'r': [4, 3], 's': [4, 4], 't': [4, 5], '.': [4, 6], '@': [4, 7], '0': [4, 8], 'u': [5, 1], 'v': [5, 2], 'w': [5, 3], 'x': [5, 4], 'y': [5, 5], 'z': [5, 6], '_': [5, 7], '/': [5, 8]}
    cursor_count = 0
    word_in_num = [[1, 1]]
    count_list = []
    cursor_count = []
    for char in word:
        word_in_num.append(keyboard[char])
    for (index, num) in enumerate(word_in_num):
        if index == 0:
            continue
        cursor_count = abs(word_in_num[index][0] - word_in_num[index - 1][0]) + abs(word_in_num[index][1] - word_in_num[index - 1][1]) + 1
        count_list.append(cursor_count)
        cursor_count = 0
    count_list = sum(count_list)
    return count_list
