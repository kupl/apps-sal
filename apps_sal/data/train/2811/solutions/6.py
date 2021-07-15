import re

def send(text):
    tmp = (ord(char) for char in text)
    tmp = (f"{x:07b}" for x in tmp)
    tmp = "".join(tmp)
    tmp = re.findall("0+|1+", tmp)
    tmp = (f"{'0' if group[0] == '1' else '00'} {'0' * len(group)}" for group in tmp)
    return " ".join(tmp)

def receive(unary):
    tmp = re.findall("(0+) (0+)", unary)
    tmp = (("0" if digit == "00" else "1") * len(count) for digit, count in tmp)
    tmp = "".join(tmp)
    tmp = re.findall(".{7}", tmp)
    tmp = (chr(int(x, 2)) for x in tmp)
    return "".join(tmp)
