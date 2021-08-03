def change_case(label, case):
    if case not in ['snake', 'kebab', 'camel'] or ('_' in label) + ('-' in label) + (label != label.lower()) > 1:
        return

    return ''.join('_' + c.lower() if c.isupper() and case == 'snake' else
                   '_' if c == '-' and case == 'snake' else

                   '-' + c.lower() if c.isupper() and case == 'kebab' else
                   '-' if c == '_' and case == 'kebab' else

                   c.upper() if label[i - 1] in '-_' and case == 'camel' else
                   '' if c in '-_' and case == 'camel' else

                   c for i, c in enumerate(label))
