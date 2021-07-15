def reverseWords(str):
    new_str=str.split()
    new_str=new_str[::-1]
    return " ".join(new_str)
