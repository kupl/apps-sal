def generate_hashtag(d):
    return (lambda b: d > '' < b == b[:139] and '#' + b)(d.title().replace(' ', ''))
