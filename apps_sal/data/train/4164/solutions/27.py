def first_non_repeating_letter(string):

    def is_unique(char):
        return string.lower().count(char.lower()) == 1
    return next((char for char in string if is_unique(char)), '')
