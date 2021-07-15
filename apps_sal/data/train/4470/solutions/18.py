nb_year=lambda p0,percent,aug,p,c=0: c if p<=p0 else nb_year(p0*(1+percent/100)+aug,percent,aug,p,c+1)
