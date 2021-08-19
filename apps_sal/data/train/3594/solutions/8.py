def is_isogram(word):
    return type(word) == str and bool(word) and (len(set(__import__('collections').Counter(__import__('re').sub('[^a-z]', '', word.lower())).values())) == 1)
