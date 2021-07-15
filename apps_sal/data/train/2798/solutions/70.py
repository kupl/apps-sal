to_alternating_case = lambda string: ''.join(map(lambda x: x.upper() if x.islower() else x.lower(), string))
