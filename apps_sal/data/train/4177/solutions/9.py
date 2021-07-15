men_from_boys=lambda a:sorted(set(a),key=lambda e:~(10**3+e)*(e%2)or -10**6+e)
