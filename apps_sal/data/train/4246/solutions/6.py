def covfefe(s):
    return (lambda cv, cf: (s + [f' {cv}', ''][cv in s]).replace(cv, cf))('coverage', 'covfefe')
