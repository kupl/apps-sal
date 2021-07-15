bouncing_ball=lambda x,y,p=1: p if x*y<=1 else bouncing_ball(x*y,y,p+1)
