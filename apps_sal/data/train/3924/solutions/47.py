def reverse_words(text):
    if len(text.split('  ')) > 1:
        return '  '.join([''.join(reversed(t)) for t in text.split('  ')])
    else:
        return ' '.join([''.join(reversed(t)) for t in text.split(' ')])
