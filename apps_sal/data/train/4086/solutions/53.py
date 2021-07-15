def first_non_consecutive(lst_input): 
    if sorted(lst_input) == list(range(min(lst_input), max(lst_input)+1)):
      return None 
    else:
      if sorted(lst_input) != list(range(min(lst_input), max(lst_input)+1)):
        for val, val2 in zip(sorted(lst_input), list(range(min(lst_input), max(lst_input)+1))):
          if val != val2:
            return val
