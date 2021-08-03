import re

ACRONYMS = {
    'KPI': "key performance indicators",
    'EOD': "the end of the day",
    'TBD': "to be decided",
    'WAH': "work at home",
    'IAM': "in a meeting",
    'OOO': "out of office",
    'NRN': "no reply necessary",
    'CTA': "call to action",
    'SWOT': "strengths, weaknesses, opportunities and threats",
}
ACRONYM_PATTERN = re.compile(r'\b[A-Z]{3,}\b')


def acronym_buster(message):
    new = ACRONYM_PATTERN.sub(lambda m: ACRONYMS.get(m.group(), m.group()), message)
    matched = ACRONYM_PATTERN.search(new)
    if matched:
        return f'{matched.group()} is an acronym. I do not like acronyms. Please remove them from your email.'
    return re.sub('[^.\s][^.]*', lambda m: m.group()[0].upper() + m.group()[1:], new)
