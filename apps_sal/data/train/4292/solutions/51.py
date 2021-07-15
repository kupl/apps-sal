def string_clean(s):
     return ''.join(['' if i in '0123456789' else i for i in s])
