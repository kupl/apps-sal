def capitalize(s, ind):
    how_about_a_list = list(s)
    for number in ind:
        if number <= len(s):
            how_about_a_list[number] = how_about_a_list[number].upper()
    return ''.join(how_about_a_list)
