def to_freud(sentence: str) -> str:
    return ' '.join(('sex' for _ in sentence.split()))
