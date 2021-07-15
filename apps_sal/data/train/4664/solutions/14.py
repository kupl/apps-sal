conference_picker=lambda v, o: o[0] if len(v)==0 else (lambda res: 'No worthwhile conferences this year!' if len(res)==0 else res[0])([c for c in o if c not in v])
