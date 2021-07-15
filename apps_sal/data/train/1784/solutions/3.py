def curry_partial(f,*initial_args):
  if not callable(f):
      return f
  exp_n_args = f.__code__.co_argcount
  given_n_args = len(initial_args)
  if exp_n_args - given_n_args > 0:
      # a lambda function that has a variable list of parameters
      # when called, it adds these parameters to the already given parameters
      # and curries the function with the combined parameters
      # In case the number of parameters is enough after that, the function will be called
      # if not, it is curried again recursively
      return lambda *args: curry_partial(f, *(initial_args + args))
  if exp_n_args == 0:
      # f is the lambda returned by curry_partial and has a variable argument list
      return f(*initial_args)
  else:
      # f is a function with a fixed number of arguments, so give it exactly how much it wants
      return f(*initial_args[:exp_n_args])
