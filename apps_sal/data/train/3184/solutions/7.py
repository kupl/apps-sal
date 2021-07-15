import re
def total_bill(s):
    return len(re.sub(r"r{5}", "rrrr", re.sub(r"\s+", "", s))) * 2

