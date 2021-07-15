import re


def sum_groups(arr):
    return len(
        re.sub("0{2,}", "0",
        re.sub("1+", lambda match: "1" if len(match.group(0)) % 2 else "0",
        "".join(str(elem % 2) for elem in arr))))
