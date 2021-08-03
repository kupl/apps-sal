def calculate(s):
    try:
        s = re.sub(r'([+*\-$])', r' \1 ', s).split()

        def doall(s_):
            while s_ in s:
                find = s.index(s_)
                t, t1 = float(s[find - 1]), float(s.pop(find + 1))
                s[find - 1] = t / t1 if s_ == "$"else t * t1 if s_ == "*"else t - t1 if s_ == "-"else t + t1
                s.pop(find)
        doall('$')
        doall('*')
        doall('-')
        doall('+')
        return float(s[0])
    except:
        return "400: Bad request"
