import re


def scratch(lottery):
    return sum(int(i[1]) for i in re.findall(r'([A-Za-z]+ )\1\1([0-9]*)', "-".join(lottery)))
