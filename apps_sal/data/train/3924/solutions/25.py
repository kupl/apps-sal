def reverse_words(text):
    return ' '.join(text[::-1].split(' ')[::-1])
    "\n    rev=text[::-1]\n    lst_rev=rev.split(' ')\n    lst=lst_rev[::-1]\n    str=' '.join(lst)\n    return str\n    "
