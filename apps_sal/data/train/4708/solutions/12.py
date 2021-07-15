def human_years_cat_years_dog_years(human_years):
  if human_years == 1: return [1, 15, 15]

  years_after_2nd = human_years - 2
  cat_years = 24 + 4*years_after_2nd
  dog_years = 24 + 5*years_after_2nd
  return [human_years, cat_years, dog_years]
