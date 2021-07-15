def remove_duplicate_words(s):
    seen = set()
    result = []
    for word in list(s.split(" ")):
        if word not in seen:
            seen.add(word)
            result.append(word)
    return " ".join(result)
