def case_id(c_str):
    if '--' in c_str or '_' in c_str and '-' in c_str:
        return "none"
    elif c_str.replace('_','').replace('-','').islower():
        if '-' in c_str:
            return "kebab"
        elif '_' in c_str:
            return "snake"
    elif '-' in c_str or '_' in c_str:
        return "none"
    return "camel"
