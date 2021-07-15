import re

def change_case(label, target):
    if ('_' in label) + ('-' in label) + (label != label.lower()) > 1:
        return
    
    if target == 'snake':
        return re.sub('([A-Z])', r'_\1', label.replace('-', '_')).lower()
    
    if target == 'kebab':
        return re.sub('([A-Z])', r'-\1', label.replace('_', '-')).lower()
    
    if target == 'camel':
        return re.sub('([_-])([a-z])', lambda m: m.group(2).upper(), label)
