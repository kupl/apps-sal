knight_or_knave = lambda said: ('Knave! Do not trust.', 'Knight!')[eval(said) if isinstance(said, str) else said]
