make_password = lambda s, x='ios': ''.join(((lambda f: '105'[f] * (f > -1))(x.find(e[0].lower())) or e[0] for e in s.split()))
