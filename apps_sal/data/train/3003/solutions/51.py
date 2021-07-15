def args_count(*args, **kwargs):
  print((locals()))
  my_params = locals()
  return len(my_params['kwargs']) + len(my_params['args'])

