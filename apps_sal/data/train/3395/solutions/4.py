def remove_duplicate_words(s):

    def f():
        seen = set()
        for word in s.split():
            if word in seen:
                continue
            seen.add(word)
            yield word
    return ' '.join(f())
