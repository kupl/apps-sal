def args_to_string(args):
    return ' '.join('-'*(len(a)>1 and 1+(len(a[0])>1))+' '.join(a) if type(a)==list else a for a in args)
