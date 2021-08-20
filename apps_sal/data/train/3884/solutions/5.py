import re
r = re.findall('\\"(\\w)(.*?)\\".*?\\"\\w(.*?)\\"', '\n    Replace all instances of "probably" to "prolly"\n    Replace all instances of "i am" to "i\'m"\n    Replace all instances of "instagram" to "insta"\n    Replace all instances of "do not" to "don\'t"\n    Replace all instances of "going to" to "gonna"\n    Replace all instances of "combination" to "combo"\n    ')


def gym_slang(s):
    for (a, b, c) in r:
        s = re.sub('(?<=[%s%s])%s' % (a, a.upper(), b), c, s)
    return s
