def solve_runes(runes):
    for i in sorted(set('0123456789') - set(runes)):
        eval_string = runes.replace('?', str(i)).replace('=', '==')
        try:
            if eval(eval_string) and eval_string[-4:] != '==00':
                return int(i)
        except:
            continue
    return -1
