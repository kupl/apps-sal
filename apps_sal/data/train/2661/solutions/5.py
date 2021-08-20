import re


def find_codwars(url):
    print(url)
    if re.search('codewars\\.com[\\?\\/].+$', url) != None:
        return False
    return re.search('(?<!\\w)(codwars\\.com[\\?\\/].+$|codwars\\.com$)', url) != None
