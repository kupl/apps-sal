def infected(s):
    population = len(s) - s.count('X')
    return population and 100 * sum((len(continent) for continent in s.split('X') if '1' in continent)) / population
