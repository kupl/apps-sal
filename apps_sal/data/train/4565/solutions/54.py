import re
def replace_dots(str):
    return ''.join(['-' if i =='.' else i for i in str])
