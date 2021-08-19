def bucket_of(said):
    (s, l) = (said.lower(), ['air', 'water', 'slime', 'sludge'])
    return l[any(['wet' in s, 'water' in s, 'wash' in s]) + any(['know' in s, 'slime' in s]) * 2]
