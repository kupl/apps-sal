def generate_hashtag(s):
    solution = '#' + ''.join([word.strip().capitalize() for word in s.split(' ')])

    if len(solution) > 1 and len(solution) < 140:
        return solution
    return False
