adjacent_element_product=lambda array:max([a*b for a,b in zip(array[:-1],array[1:])])
