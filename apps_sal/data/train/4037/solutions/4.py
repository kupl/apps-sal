import re
def detect_operator(num):
    d = {r"0(66|50|9[59])": "MTS",
        r"0[69]3": "Life:)",
        r"0(9[6-8]|67)": "Kyivstar",
        r"068": "Beeline",
        r"039": "Golden Telecom"
        }
    for temp in d:
        if re.fullmatch(temp, num[1:4]):
            return d[temp]
    return "no info"
