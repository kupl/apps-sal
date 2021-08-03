def is_tune(notes=None):
    if not notes:
        return False

    major_scale = [0, 2, 4, 5, 7, 9, 11]

    def is_in_key_of(_notes, n):
        return all((note + n) % 12 in major_scale for note in _notes)

    tonic = min(notes)
    _notes = [n - tonic for n in notes]
    return any(is_in_key_of(_notes, n) for n in major_scale)
