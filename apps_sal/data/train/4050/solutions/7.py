import re

d = {
    "KPI": "key performance indicators", "EOD": "the end of the day", "TBD": "to be decided",
    "WAH": "work at home", "IAM": "in a meeting", "OOO": "out of office",
    "NRN": "no reply necessary", "CTA": "call to action", "SWOT": "strengths, weaknesses, opportunities and threats"
}


def acronym_buster(s):
    a = []

    def f(x):
        x = x[0]
        if x.isupper() and len(x) > 2:
            if x not in d:
                a.append(x)
            x = d.get(x, "")
        return x
    s = re.sub(r"^.|[!?.] .", lambda x: x[0].upper(), re.sub(r"\w+", f, s))
    return f"{a[0]} is an acronym. I do not like acronyms. Please remove them from your email." if a else s
