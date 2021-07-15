import re


def siegfried(week, txt):
    weeks_have_passed = {0: week_one, 1: week_two, 2: week_three, 3: week_four, 4: week_five}

    for counter in range(0, week):

        txt = weeks_have_passed[counter](txt)
    
    return txt

def week_one(txt):

    letter_list = list(txt)

    copy_reverse_letter_list = letter_list.copy()


    last_letter = ''

    count = -1

    for letter in copy_reverse_letter_list[::-1]:

        lowercase_letter = letter.lower()

        if lowercase_letter == 'c':
            lowercase_letter += last_letter

            if letter.isupper():
                dict_to_know = {'ci': 'S', 'ce': 'S', 'ch': 'C'}
                to_return = 'K'
            else:
                dict_to_know = {'ci': 's', 'ce': 's', 'ch': 'c'}
                to_return = 'k'

            letter_list[count] = dict_to_know.get(lowercase_letter, to_return)

        count -= 1
        last_letter = letter

    final_txt = ''.join(letter_list)

    return final_txt


def week_two(txt):

    letter_list = list(txt)

    copy_letter_list = letter_list.copy()
    copy_letter_list.append('')

    fix_position = 0

    for counter, letter in enumerate(copy_letter_list[:-1]):

        lowercase_letter = letter.lower()

        next_letter = copy_letter_list[counter+1]
        lowcase_next_letter = next_letter.lower()

        if lowercase_letter == 'p' and lowcase_next_letter == 'h':

            counter -= fix_position

            if letter.isupper():
                to_change = 'F'
            else:
                to_change = 'f'

            letter_list[counter: counter + 2] = to_change

            fix_position += 1

    new_txt = ''.join(letter_list)

    return new_txt


def week_three(txt):
    trailling_e = r'[a-zA-Z]{3,}e\b'

    trailling_list = re.findall(trailling_e, txt)

    new_txt = txt

    for trailling_e_word in trailling_list:
        new_txt = new_txt.replace(trailling_e_word, trailling_e_word[:-1])

    letter_list = list(new_txt)

    copy_letter_list = letter_list.copy()

    last_letter = ''

    position = -1

    for letter in copy_letter_list[::-1]:

        lowercase_letter = letter.lower()

        if lowercase_letter == last_letter and lowercase_letter.isalpha():

            del letter_list[position+1]

            position += 1

        last_letter = lowercase_letter

        position -= 1

    final_txt = ''.join(letter_list)

    return final_txt



def week_four(txt):

    letter_list = list(txt)

    copy_reverse_letter_list = letter_list.copy()

    last_letter = ''

    counter = -1

    for letter in copy_reverse_letter_list[::-1]:

        lowercase_letter = letter.lower()

        if lowercase_letter == 'w' or lowercase_letter == 't' and last_letter == 'h':
            lowercase_letter += last_letter

            if letter.isupper():
                dict_to_know = {'wr': 'R', 'wh': 'V', 'th': 'Z'}
                lonely_w = 'V'
            else:
                dict_to_know = {'wr': 'r', 'wh': 'v', 'th': 'z'}
                lonely_w = 'v'

            possible_last_letters = {'h', 'r'}

            if last_letter in possible_last_letters:
                letter_list[counter: counter+2] = dict_to_know[lowercase_letter]
                counter += 1

            else:
                letter_list[counter] = lonely_w

        counter -= 1
        last_letter = letter

    final_txt = ''.join(letter_list)

    return final_txt


def week_five(txt):
    letter_list = list(txt)

    copy_reverse_letter_list = letter_list.copy()

    last_letter = ''

    counter = -1

    for letter in copy_reverse_letter_list[::-1]:
        lowercase_letter = letter.lower()

        if lowercase_letter == 'o' and last_letter == 'u':
            lowercase_or_uppercase = {'o': 'u', 'O': 'U'}

            letter_list[counter: counter+2] = lowercase_or_uppercase[letter]

            counter += 1

        elif lowercase_letter == 'a' and last_letter == 'n':
            lowercase_or_uppercase_2 = {'a': 'u', 'A': 'U'}

            letter_list[counter] = lowercase_or_uppercase_2[letter]

        last_letter = lowercase_letter

        counter -= 1

    first_txt = ''.join(letter_list)

    re_to_find_ing = r'[a-zA-Z]{1,}ing\b'

    all_words_ending_with_ing = re.findall(re_to_find_ing, first_txt)

    second_txt = first_txt

    for word in all_words_ending_with_ing:
        new_word = word[:-1] + 'k'
        second_txt = second_txt.replace(word, new_word)

    re_to_find_sm = r'\b[sS][mM][a-zA-Z]*'


    all_words_starting_with_sm = re.findall(re_to_find_sm, second_txt)

    third_txt = second_txt

    for word in all_words_starting_with_sm:
        new_word = word[0] + 'ch' + word[1:]
        third_txt = third_txt.replace(word, new_word)

    final_txt = third_txt

    return final_txt
