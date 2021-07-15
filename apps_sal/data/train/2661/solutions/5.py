import re
def find_codwars(url):
    print(url)
    if(re.search(r"codewars\.com[\?\/].+$",url) != None):
        return False
    return re.search(r"(?<!\w)(codwars\.com[\?\/].+$|codwars\.com$)",url) != None
