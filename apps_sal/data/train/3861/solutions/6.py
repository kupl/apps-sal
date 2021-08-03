import re


def fire_and_fury(tweet):
    if re.search(r'[^EFIRUY]', tweet):
        return 'Fake tweet.'
    tweet = "".join(re.findall(r'FIRE|FURY', tweet))
    return re.sub(r'(FIRE)+|(FURY)+', change, tweet).strip(" ") if tweet else 'Fake tweet.'


def change(m):
    m = m.group()
    if 'FURY' in m:
        return "I am " + "really " * (m.count("FURY") - 1) + "furious." + " "
    if 'FIRE' in m:
        return "You " + "and you " * (m.count("FIRE") - 1) + "are fired!" + " "
