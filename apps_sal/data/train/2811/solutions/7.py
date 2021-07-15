import re

def send(s):
    return " ".join(f"{'0' if x[0] == '1' else '00'} {'0' * len(x)}" for x in re.findall("0+|1+", "".join(f"{x:07b}" for x in map(ord, s))))

def receive(s):
    return re.sub(".{7}", lambda x: chr(int(x.group(), 2)), "".join(("1" if x == "0" else "0") * len(y) for x, y in re.findall("(0+) (0+)", s)))
