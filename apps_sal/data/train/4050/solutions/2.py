import re

D = {"KPI": "key performance indicators",
     "EOD": "the end of the day",
     "TBD": "to be decided",
     "WAH": "work at home",
     "IAM": "in a meeting",
     "OOO": "out of office",
     "NRN": "no reply necessary",
     "CTA": "call to action",
     "SWOT": "strengths, weaknesses, opportunities and threats"}

acronym = re.compile(r"(?:^|(?<=\W))[A-Z]{3,}(?=\W|$)")
capital = re.compile(r"(?:^|(?<=\.\s))[a-z]")

def acronym_buster(message):
    try:
        return capital.sub(lambda w: w.group().upper(), acronym.sub(lambda w: D[w.group()], message))
    except Exception as e:
        return f"{str(e)[1:-1]} is an acronym. I do not like acronyms. Please remove them from your email."
