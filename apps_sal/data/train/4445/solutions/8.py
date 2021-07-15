#https://www.codewars.com/kata/5c765a4f29e50e391e1414d4/train/python
def is_haiku(text):
    is_haiku = True
    vowel_list = ["a", "e", "i", "o", "u", "y"]
    haiku = text.splitlines()
    if len(haiku) != 3:
        return False
    for line in range(0,3):
        syllable = 0
        haiku[line] = haiku[line].split(" ") 
        for word in haiku[line]:
            current_syllable = 0
            silent_e = False
            word = word.lower()
            word = "".join(filter(str.isalnum, word))
            if len(word) == 1 and word in vowel_list:
                current_syllable += 1
            elif len(word) >= 2:
                if word[0] in vowel_list:
                    current_syllable += 1
                    silent_e = True
                for position in range(1,len(word)):
                    if (word[position] in vowel_list) and (word[position-1] not in vowel_list):
                        current_syllable += 1
                        silent_e = True
                if current_syllable != 1 and silent_e == True and word[-1] == "e" and word[-2] not in vowel_list:
                    current_syllable -= 1
            syllable += current_syllable
        if line == 0 or line == 2:
            if syllable != 5:
                is_haiku = False
        elif line == 1:
            if syllable != 7:
                is_haiku = False
        if is_haiku == False:
            return is_haiku
    return is_haiku
