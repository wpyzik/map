import folium
import pandas

data= pandas.read_csv("Volcanoes.txt")
lat= list(data["LAT"])
lon= list(data["LON"])
name= list(data["NAME"])
elev = list(data["ELEV"])

def color_producer(elevation):
    if el < 1500:
        return 'green'
    elif 1500 <= el < 3000:
        return 'orange'
    else:
        return 'red'

map = folium.Map(location=[38.58, -99.09], zoom_start=5, titles="Stamen Terrain")

fg= folium.FeatureGroup(name="My Map")

for lt,ln,nm,el in zip(lat,lon,name,elev):
    fg.add_child(folium.Marker(location= [lt,ln], popup= nm.title() + "\n " "%s m" %el, icon=folium.Icon(color= color_producer(el))))

map.add_child(fg)

map.save("Map1.html")
