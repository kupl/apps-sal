import re
def wheres_wally(string):
    match=re.search(r' Wally\b'," "+string)
    if match is None:
        return -1
    else:
        return match.start()
