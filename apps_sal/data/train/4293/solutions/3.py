calculate_1RM=lambda w,r:[[round(max(w*(1+(r/30)),100*w/(101.3-(2.67123*r)),w*r**0.10)),0][r==0],w][r==1]
