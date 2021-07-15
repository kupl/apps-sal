def debug(s):
    return 'bugs'.join(w.replace('bug', '') for w in s.split('bugs'))
