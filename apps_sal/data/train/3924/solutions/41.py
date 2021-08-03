def reverse_words(str): return ' '.join(''.join(j for j in i[::-1]) for i in str.split(' '))
