def remove_duplicate_words(s):
    split = s.split(' ')
    end = []
    for word in split: 
        if word in end:
            continue;
        end.append(word)
    return ' '.join(end)

