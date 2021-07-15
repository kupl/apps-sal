cooking_time=lambda n,m,s,p:'{} minutes {} seconds'.format(*divmod(-(-(m*60+s)*int(n[:-1])//int(p[:-1])),60))
