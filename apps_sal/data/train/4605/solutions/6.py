import re


def replace_dashes_as_one(s):
    return replace_dashes_as_one(re.sub('- *-', '-', s)) if re.search('- *-', s) else s
