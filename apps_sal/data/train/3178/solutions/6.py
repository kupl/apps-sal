import re
def pete_talk(speech, ok = []):
    ok = {v.lower() for v in ok}
    def repl(Match):
        s = Match[0]
        i = Match.start()
        
        
        if i == 0 or (i >= 2 and speech[i - 2] in '.!?'):
            s = s.capitalize()
        else:
            s = s.lower()
        n = len(s)
        if n <= 2 or s.lower() in ok:
            return s
        return s[0] + '*' * (n - 2) + s[-1]
    return re.sub('\w+', repl, speech)
