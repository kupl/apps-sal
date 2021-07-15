import re
r = re.findall(r"\"(\w)(.*?)\".*?\"\w(.*?)\"", """
    Replace all instances of "probably" to "prolly"
    Replace all instances of "i am" to "i'm"
    Replace all instances of "instagram" to "insta"
    Replace all instances of "do not" to "don't"
    Replace all instances of "going to" to "gonna"
    Replace all instances of "combination" to "combo"
    """)

def gym_slang(s):
    for a, b, c in r: s = re.sub("(?<=[%s%s])%s" % (a, a.upper(), b), c, s)
    return s
