def case_id(s):
    if '--' in s or '_' in s and '-' in s:
        return 'none'
    if s.replace('_','').replace('-','').islower():
        if '-' in s: return 'kebab'
        if '_' in s: return 'snake'
    if '-' in s or '_' in s: 
        return 'none'
    return 'camel'
