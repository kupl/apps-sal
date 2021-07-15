import re

know_acronyms = {
    'KPI': "key performance indicators",
    'EOD': "the end of the day",
    'TBD': "to be decided",
    'WAH': "work at home",
    'IAM': "in a meeting",
    'OOO': "out of office",
    'NRN': "no reply necessary",
    'CTA': "call to action",
    'SWOT': "strengths, weaknesses, opportunities and threats"
}

def acronym_buster(message):
    unknow_acronyms = []
    replace_or_store = lambda a: a in know_acronyms and know_acronyms[a] or unknow_acronyms.append(a)
    cleaned = re.sub(r'\b[A-Z]{3,}\b', lambda m: replace_or_store(m.group()), message)
    if unknow_acronyms:
        return '%s is an acronym. I do not like acronyms. Please remove them from your email.' % unknow_acronyms[0]
    else:
        return re.sub('(^|[.!?]) *\w', lambda m: m.group().upper(), cleaned)
