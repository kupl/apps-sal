import re
from functools import reduce

_ACRONYMS = {
    'KPI': 'key performance indicators',
    'EOD': 'the end of the day',
    'EOP': 'the end of the day',
    'TBD': 'to be decided',
    'WAH': 'work at home',
    'IAM': 'in a meeting',
    'OOO': 'out of office',
    'NRN': 'no reply necessary',
    'CTA': 'call to action',
    'SWOT': 'strengths, weaknesses, opportunities and threats'}

_ACRONYM_PATTERN = re.compile(r'\b[A-Z]{3,}\b')
_CAPITAL_PATTERN = re.compile(r'(?:\. |^)([a-z])')
def _CAPITAL_FIX(match): return '{}'.format(match.group(0).upper())


def acronym_buster(message):
    message = reduce(lambda msg, item: msg.replace(*item), _ACRONYMS.items(), message)
    try:
        acro = next(_ACRONYM_PATTERN.finditer(message)).group(0)
        return '{} is an acronym. I do not like acronyms. Please remove them from your email.'.format(acro)
    except StopIteration:
        return _CAPITAL_PATTERN.sub(_CAPITAL_FIX, message)
