import re


def acronym_buster(s):
    (d, temp) = ({'KPI': 'key performance indicators', 'EOD': 'the end of the day', 'TBD': 'to be decided', 'WAH': 'work at home', 'IAM': 'in a meeting', 'OOO': 'out of office', 'NRN': 'no reply necessary', 'CTA': 'call to action', 'SWOT': 'strengths, weaknesses, opportunities and threats'}, [])
    while re.search('\\b[A-Z]{3,}\\b', s):
        r = re.search('\\b[A-Z]{3,}\\b', s)
        arn = r.group()
        (start, end) = r.span()
        if arn in d:
            s = s[:start] + d[arn] + s[end:]
        else:
            return f'{arn} is an acronym. I do not like acronyms. Please remove them from your email.'
    return '. '.join([i[0].upper() + i[1:] for i in s.split('. ')])
