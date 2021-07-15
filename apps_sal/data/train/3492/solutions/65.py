polish_letter = {"ą": "a",
"ć": "c",
"ę": "e",
"ł": "l",
"ń": "n",
"ó": "o",
"ś": "s",
"ź": "z",
"ż": "z"}

def correct_polish_letters(st):
    new_list = []
    for letter in st:
        if letter in polish_letter:
            letter = polish_letter[letter]
        new_list.append(letter)
    return "".join(new_list)

