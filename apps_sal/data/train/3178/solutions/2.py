import re


def pete_talk(speech, ok=[]):
    ok = [i.lower() for i in ok]

    def repl(m):
        if m.group('word') not in ok:
            return m.group('word')[0] + '*' * len(m.group('reppart')) + m.group('word')[-1]
        else:
            return m.group('word')

    replaced = re.sub('(?P<word>[\w](?P<reppart>[\w]+)[\w])', repl, speech.lower())
    capitalized = re.sub('(?P<sent>[.!?]+\s*|\A\s*)(?P<word>\s*[a-z])', lambda m: m.group('sent') + m.group('word').capitalize(), replaced)
    return capitalized
