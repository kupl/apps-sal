is_odd_heavy=lambda a:max([n for n in a if-~n%2]or[float('-inf')])<min([n for n in a if n%2]or[float('-inf')])
