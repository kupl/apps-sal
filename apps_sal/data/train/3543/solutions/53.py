import re
def increment_string(strng):
    x = re.findall(".*\D(\d*)", 'a'+strng)
    if not x or not x[0] :
        return strng + '1'
    return [strng[:-len(r)] + str(int(r)+1).zfill(len(r)) for r in x][0]
