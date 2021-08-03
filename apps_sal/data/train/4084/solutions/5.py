def alex_mistakes(n, l):
    mistakes = 0
    push_time = 0
    while push_time < l - n * 6:
        push_time += 5 * 2**mistakes
        if push_time > l - n * 6:
            return mistakes
        mistakes += 1
    else:
        return mistakes
