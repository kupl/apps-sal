def correct(string):
    return "".join("I" if k == "1" else k for k in ("O" if j == "0" else j for j in ("S" if i == "5" else i for i in string)))
