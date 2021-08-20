def vowel_start(stg):
    return ''.join((f"{(' ' if c in 'aeiou' else '')}{c}" for c in stg.lower() if c.isalnum())).lstrip()
