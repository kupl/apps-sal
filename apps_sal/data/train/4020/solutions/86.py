import re
def validate_hello(greetings):
    tpl = r'(?i)(\bhello\b)|(\bhallo\b)|(\bciao\b)|(\bsalut\b)|(\bhola\b)|(\bahoj\b)|(\bczesc\b)'
    return True if re.search(tpl, greetings) != None else False
