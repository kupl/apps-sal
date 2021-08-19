def generate_hashtag(s):
    output = '#' + s.title().replace(' ', '')
    return output if len(output) <= 140 and output != '#' else False
