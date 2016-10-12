
from shapely.geometry import Point
from shapely.prepared import prep

print 'populating'
pts =[]
for t in range (0,1000000):
    pts.append(Point(t,1+t))

print 'preparing'
polygon = Point(0.0, 0.0).buffer(5.0)
prepared_polygon = prep(polygon)
print 'searching'

hits = filter(prepared_polygon.contains,pts)
print len(hits)

