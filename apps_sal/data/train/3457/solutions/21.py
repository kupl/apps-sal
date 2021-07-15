final_grade=lambda e,p:[0,75,90,100][(3*(e>90 or p>10) or 2*(e>75 and p>4) or (e>50 and p>1))]
