def ka_co_ka_de_ka_me(s):
    return __import__('re').sub('(?i)(\\b(?=\\w)|(?<=[aeiou])\\B(?![aeiou]))', 'ka', s)
