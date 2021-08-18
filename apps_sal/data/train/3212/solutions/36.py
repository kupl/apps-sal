def generate_hashtag(s: str):
    number_of_chars = len(s)
    if s and number_of_chars < 140:
        words_list = [word.capitalize() for word in s.split()]
        words = ['
        result = ''.join(words)
        return result
    else:
        return False
