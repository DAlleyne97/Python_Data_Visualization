"""World map that highlights North, Central, and South America"""
import pygal

#Declaring a map and giving it a title
wm = pygal.maps.world.World()
wm.title = 'North, Central and South America' 

#Adds the labels and countries we want to focus on
wm.add('North America', ['ca', 'mx', 'us'])
wm.add('Central America', ['bz', 'cr', 'gt', 'hn', 'ni', 'pa', 'sv'])
wm.add('South America', ['ar', 'bo', 'br', 'cl', 'co', 'ec', 'gf', 
    'gy', 'pe', 'py', 'sr', 'uy', 've'])

#Creates the file containing the map
wm.render_to_file('AmericasMap/americas.svg')