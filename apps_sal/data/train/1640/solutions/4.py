def filter_lowercase(character_in_s):
    lowercase_alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m",
                          "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]

    if(character_in_s in lowercase_alphabet):
        return True
    else:
        return False


def sort_mix(a):
    return len(a)


def order_alphabetically_ascendent(elem):
    if elem[:1] == "=":
        return 2
    elif elem[:1] == "1":
        return 0
    elif elem[:1] == "2":
        return 1


def mix(s1, s2):
    lowercase_alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m",
                          "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
    characters_in_s1 = []
    characters_in_s2 = []

    amount_of_each_letter_in_s1 = []
    amount_of_each_letter_in_s2 = []
    where_is_maximum = []
    maximum = []

    letters_used_with_prefix = []
    string_to_return = ""

    different_lengths = []
    array_of_letters_with_the_same_length = []

    for character in s1:
        characters_in_s1.append(character)
    for character in s2:
        characters_in_s2.append(character)

    lowercase_letters_in_s1 = list(filter(filter_lowercase, characters_in_s1))
    lowercase_letters_in_s2 = list(filter(filter_lowercase, characters_in_s2))

    for alphabet_letter in lowercase_alphabet:
        lowercase_letters_in_s = []
        i = len(amount_of_each_letter_in_s1)
        string_to_append = ""

        amount_of_each_letter_in_s1.append(lowercase_letters_in_s1.count(alphabet_letter))
        lowercase_letters_in_s.append(lowercase_letters_in_s1.count(alphabet_letter))

        amount_of_each_letter_in_s2.append(lowercase_letters_in_s2.count(alphabet_letter))
        lowercase_letters_in_s.append(lowercase_letters_in_s2.count(alphabet_letter))

        maximum.append(max(lowercase_letters_in_s))

        if lowercase_letters_in_s2.count(alphabet_letter) == lowercase_letters_in_s1.count(alphabet_letter):
            where_is_maximum.append("b")
        elif lowercase_letters_in_s1.count(alphabet_letter) > lowercase_letters_in_s2.count(alphabet_letter):
            where_is_maximum.append("1")
        elif lowercase_letters_in_s2.count(alphabet_letter) > lowercase_letters_in_s1.count(alphabet_letter):
            where_is_maximum.append("2")

        if maximum[i] > 1:
            if where_is_maximum[i] == "b":
                string_to_append = "=:" + lowercase_alphabet[i] * maximum[i]
            elif where_is_maximum[i] != "b":
                string_to_append += str(where_is_maximum[i]) + ":" + lowercase_alphabet[i] * maximum[i]

            letters_used_with_prefix.append(string_to_append)

    letters_used_with_prefix = sorted(letters_used_with_prefix, key=lambda conjunto: (len(conjunto)), reverse=True)

    for string in letters_used_with_prefix:
        if len(string) not in different_lengths:
            different_lengths.append(len(string))

    length = len(different_lengths)

    while length > 0:
        letters_with_the_same_length = []
        for letter_used_with_prefix in letters_used_with_prefix:
            if len(letter_used_with_prefix) == different_lengths[length - 1]:
                letters_with_the_same_length.append(letter_used_with_prefix)
        letters_with_the_same_length = sorted(letters_with_the_same_length, key=order_alphabetically_ascendent)
        array_of_letters_with_the_same_length.append(letters_with_the_same_length)

        length = length - 1

    array_of_letters_with_the_same_length.reverse()

    for subarray in array_of_letters_with_the_same_length:
        for item in subarray:
            string_to_return += item + "/"

    string_to_return = string_to_return[:-1]
    return(string_to_return)
