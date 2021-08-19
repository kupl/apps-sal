from functools import partial
import re


def gym_slang(phrase):

    def repl(match):

        def check_upper(word, match):
            return word.capitalize() if match[0].isupper() else word
        check = partial(check_upper, match=match.group())
        if match.group() == match.group(1):
            return check('prolly')
        if match.group() == match.group(2):
            return check("i'm")
        if match.group() == match.group(3):
            return check('insta')
        if match.group() == match.group(4):
            return check("don't")
        if match.group() == match.group(5):
            return check('gonna')
        if match.group() == match.group(6):
            return check('combo')
    return re.sub('(?i)(probably)|(i am)|(instagram)|(do not)|(going to)|(combination)', repl, phrase)
