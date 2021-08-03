def validate_word(word):
    word = word.lower()
    arr = list(set(word))
    for i in range(1, len(arr)):
        if word.count(arr[i]) != word.count(arr[i - 1]):
            return False
    return True
