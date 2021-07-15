def show_me(name):
    return all(word.isalpha() and word.capitalize() == word for word in name.split('-'))
