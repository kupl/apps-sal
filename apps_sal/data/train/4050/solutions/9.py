import re


def acronym_buster(s):

    def f(x):
        return all((len(x) > 2 and i.isupper() for i in x))
    d = {'KPI': 'key performance indicators', 'EOD': 'the end of the day', 'TBD': 'to be decided', 'WAH': 'work at home', 'IAM': 'in a meeting', 'OOO': 'out of office', 'NRN': 'no reply necessary', 'CTA': 'call to action', 'SWOT': 'strengths, weaknesses, opportunities and threats'}
    for i in re.findall("[\\w']+", s):
        if f(i):
            if i not in d:
                return f'{i} is an acronym. I do not like acronyms. Please remove them from your email.'
            s = s.replace(i, d[i], 1)
    return '. '.join((i[0].upper() + i[1:] for i in s.split('. ')))
