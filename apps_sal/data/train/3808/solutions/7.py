def knight_or_knave(said): return ('Knave! Do not trust.', 'Knight!')[eval(said) if isinstance(said, str) else said]
