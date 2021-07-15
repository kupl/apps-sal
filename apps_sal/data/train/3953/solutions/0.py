def longest_word(letters):
    try:
        word_list = [w for w in words if all(w.count(c) <= letters.count(c) for c in w)]
        largest = sorted([w for w in word_list if len(w) == len(max(word_list, key=len))])
        return largest if largest else None
    except:
        return None
