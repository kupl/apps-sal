def increment_string(strng):
    import re
    try:
        h = re.findall("\d+$", strng)[0]
        return re.sub("\d+$", str(int(h)+1).zfill(len(h)), strng)
    except:
        return strng + "1"
