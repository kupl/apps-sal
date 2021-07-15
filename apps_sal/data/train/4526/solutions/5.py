day_plan=lambda h,t,d:t*d>h*60and"You're not sleeping tonight!"or([(h*60-t*d)//(t-1+1e-9),d]*t)[1:]
