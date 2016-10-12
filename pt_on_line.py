from shapely.geometry import LineString, Point

line = LineString([(1,1),(10,3)])       
p = Point (6,5)

# Length along line that is closest to the point
print(line.project(p))

# Now combine with interpolated point on line
np = line.interpolate(line.project(p))
print(np)  # POINT (5 7)
