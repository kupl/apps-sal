def to_freud(sentence):
    res = ["sex"]
    a = list(sentence).count(" ")
    for i in range(a):
        res.append("sex")
    return " ".join(res)
