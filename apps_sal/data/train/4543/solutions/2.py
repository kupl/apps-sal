form = '#'+'{0:0>2}'*3
shades_of_grey=lambda n:[form.format(hex(i)[2:])for i in range(1,min(n+1,255))]
