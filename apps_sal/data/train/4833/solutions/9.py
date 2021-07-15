replace_exclamation = lambda s: ''.join("!" if c in "aiueoAIUEO" else c for c in s)
