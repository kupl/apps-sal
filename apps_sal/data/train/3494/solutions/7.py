from string import punctuation


def pig_it(text):
    words = text.split(' ')
    return ' '.join(
        [
            '{}{}ay'.format(
                word[1:],
                word[0]
            ) if word not in punctuation else word for word in words
        ]
    )
