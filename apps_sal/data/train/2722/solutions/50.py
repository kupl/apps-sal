def remove_url_anchor(url):
    char_list = list(url)
    anchor_index = len(char_list)
    for number in range(0, len(char_list)):
        if (char_list[number] == "#"):
            anchor_index = number
    without_anchor = "".join(char_list[number] for number in range(0, anchor_index))
    return without_anchor
