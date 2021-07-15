import re

def toUnderScore(name):
    if not name: return ""
    a = '_'.join([s for s in re.split(r'(_?[A-Z][a-z]*_?|[0-9]+[a-z]*)', re.sub('_', '', name)) if s])
    if name[0] == '_': a = '_' + a
    if name[-1] == '_': a = a + '_'
    return a
