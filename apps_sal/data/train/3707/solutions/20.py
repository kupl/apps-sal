def sorter(textbooks):
    subjects = dict((sub.lower(), sub) for sub in textbooks)
    return [subjects[sub] for sub in sorted(subjects.keys())]
