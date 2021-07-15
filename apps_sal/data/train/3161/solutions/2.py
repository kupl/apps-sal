def select(s):
    s_ = s.split(", ")
    li = sum([[j[1:], s_[i+1] if i < len(s_)-1 else "X"] for i, j in enumerate(s_) if j[0]=="!"],[])
    return ", ".join([i for i in s_ if i not in li and i[0] != "!"])
