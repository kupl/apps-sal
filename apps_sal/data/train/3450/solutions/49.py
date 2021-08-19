def array(string):
    if string == "" or len(string) < 5:
        return None
    word = string.split(",")
    res = []
    for i in range(1, len(word) - 1):
        res.append(word[i])
    if len(res) < 1:
        return None
    else:
        return " ".join(res)

    # your code here
