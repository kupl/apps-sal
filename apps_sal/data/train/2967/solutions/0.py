bin2hex = {"0000": "0", "0001": "1", "0010": "2", "0011": "3",
           "0100": "4", "0101": "5", "0110": "6", "0111": "7",
           "1000": "8", "1001": "9", "1010": "a", "1011": "b",
           "1100": "c", "1101": "d", "1110": "e", "1111": "f"}
hex2bin = {v: k for k, v in bin2hex.items()}


def bin_to_hex(s, res=""):
    s = "0" * (4 - len(s) % 4) + s
    while s:
        res += bin2hex[s[:4]]
        s = s[4:]
    return res.lstrip("0") or "0"


def hex_to_bin(s, res=""):
    while s:
        res += hex2bin[s[0].lower()]
        s = s[1:]
    return res.lstrip("0") or "0"
