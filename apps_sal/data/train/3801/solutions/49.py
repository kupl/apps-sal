def words_to_marks(s):
    s = s.lower()
    sum_char = 0
    characters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    for char in s:
        if char in characters:
            number = characters.index(char) + 1
            sum_char += number
    return sum_char
