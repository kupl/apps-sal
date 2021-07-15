human_years_cat_years_dog_years = lambda h: [h] + [15*(h>=1)+9*(h>=2)+(h-2)*y*(h>2) for y in [4,5]] 
