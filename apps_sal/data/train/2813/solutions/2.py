chars = "_zyxwvutsrqponmlkjihgfedcba!? "

def switcher(arr):
    return "".join(chars[int(i)] for i in arr if i != "0")
