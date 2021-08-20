def remove_duplicate_words(s):
    return ' '.join((s.split()[i] for i in range(len(s.split())) if s.split()[i] not in s.split()[0:i]))
