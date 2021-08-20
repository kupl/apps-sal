import re


def alan_annoying_kid(s):
    action = s[8:-1]
    d = ['did', "didn't"]["didn't" not in action]
    present = re.sub('ed$', '', re.search('^\\w+', action.replace("didn't ", '')).group())
    return "I don't think you " + action + ' today, I think you ' + d + ' ' + present + [' it!', ' at all!'][d == "didn't"]
