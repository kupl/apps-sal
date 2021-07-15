def decode(string_):
    if not isinstance(string_, str):
        return "Input is not a string"
    return string_.translate(str.maketrans("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ", "zyxwvutsrqponmlkjihgfedcbaZYXWVUTSRQPONMLKJIHGFEDCBA"))
