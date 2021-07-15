import string
import re


def spreadsheet(s):
    if re.match(r"^R\d+C\d+$", s):
        return convert_to_ss(s)
    else:
        return convert_to_rc(s)

def convert_to_rc(s: str) -> str:
    ind = re.search(r"\d", s).span()[0]
    letters = s[:ind]
    nums = s[ind:]
    cols = 0
    for i in range(len(letters)):
        if i != len(letters) - 1:
            cols += (string.ascii_uppercase.find(letters[i]) + 1) * 26 ** (len(letters) - i - 1)
        else:
            cols += (string.ascii_uppercase.find(letters[i]) + 1)
    return f"R{nums}C{cols}"

def convert_to_ss(s: str) -> str:
    ind = s.find("C")
    rows = s[1:ind]
    cols = int(s[ind+1:])
    res_col = ""
    while cols > 0:
        cols, rem = cols // 26, cols % 26
        if res_col and res_col[0] == "Z":
            if rem == 1:
                break
            else:
                res_col = string.ascii_uppercase[rem - 2] + res_col
        else:
            res_col = string.ascii_uppercase[rem - 1] + res_col
        print(cols, rem)
    return f"{res_col}{rows}"
