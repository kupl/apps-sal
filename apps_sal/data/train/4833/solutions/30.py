def replace_exclamation(s):
   return "".join(['!' if _ in 'aeiouAEIOU' else _ for _ in s])
