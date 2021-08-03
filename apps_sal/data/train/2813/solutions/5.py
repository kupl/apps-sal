STR = "+zyxwvutsrqponmlkjihgfedcba!? "


def switcher(arr):
    return "".join(STR[int(x)] for x in arr).replace("+", "")
