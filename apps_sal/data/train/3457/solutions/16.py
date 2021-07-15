final_grade=lambda e,p:[0,75,90,100][sum([e>90or p>10,(e>75and p>4)or(e>90or p>10),(e>50and p>1)or(e>90or p>10)])]
