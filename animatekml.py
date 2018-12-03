import simplekml
import glob
import datetime

kml = simplekml.Kml()

currentdate = datetime.datetime.utcnow()

def date_to_str(date):
    return date.strftime("%Y-%m-%dT%H:%M:%S")

for i, image in enumerate(sorted(glob.glob("images/*.png"))):
    time = image.split("/")[-1][:-4]
    ground1 = kml.newgroundoverlay(name='Europe ' + str(i))
    ground1.icon.href = image
    # ground1.gxlatlonquad.coords = [(-180,-90),(180,-90),(180,90),(-180,90)]
    ground1.latlonbox.north = 55.4
    ground1.latlonbox.south = 37.5
    ground1.latlonbox.east =  16
    ground1.latlonbox.west =  -12
    d = currentdate + datetime.timedelta(hours=6 * i)
    ground1.timespan.begin = date_to_str(d)
    d_1 = currentdate + datetime.timedelta(hours=5 + 6*i)
    ground1.timespan.end =date_to_str(d_1)

# ground2 = kml.newgroundoverlay(name='Blue Marble - Feb')
# ground2.icon.href = 'http://mw1.google.com/mw-earth-vectordb/kml-samples/bmng12/files/BMNG-Feb.jpg'
# ground2.gxlatlonquad.coords = [(-180,-90),(180,-90),(180,90),(-180,90)]
# ground2.timespan.begin = "2004-02-01"
# ground2.timespan.end = "2004-02-29"

# ...and so on with the other months

kml.save("meteo.kml")
