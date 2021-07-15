close_to_zero=lambda t:min(map(int,t.split()),key=lambda n:(abs(n),-n),default=0)
