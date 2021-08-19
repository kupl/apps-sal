def is_palindrome(s):
    s_low = s.lower()
    if len(s) == 1:
        return True
    elif len(s) % 2 == 0:
        half = int(len(s) / 2)
        word_part_1 = s_low[:half]
        word_part_2 = s_low[half:][::-1]
        if word_part_1 == word_part_2:
            return True
        else:
            return False
    elif len(s) % 2 == 1:
        half2 = int(len(s) / 2)
        word_part_3 = s_low[:half2]
        word_part_4 = s_low[half2 + 1:][::-1]
        if word_part_3 == word_part_4:
            return True
        else:
            return False
