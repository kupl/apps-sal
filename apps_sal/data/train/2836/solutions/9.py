def find_screen_height(width, ratio):
    return "{}x{}".format(width, int(((width / int(ratio.split(':')[0])) * int(ratio.split(':')[1]))))
