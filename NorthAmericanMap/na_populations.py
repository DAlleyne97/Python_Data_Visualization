"""Map containing populations of the three countries in North America"""
import pygal

wm = pygal.maps.world.World()
wm.title = 'Populations of Countries in North America'

#Adding lable, country and the population of each
wm.add('North America', {'ca' : 34126000, 'us' : 309349000, 'mx' : 113423000})

wm.render_to_file('NorthAmericanMap/na_populations.svg')