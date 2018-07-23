###functions which complete the problems from the first exercises.

import shapely
import pandas
from shapely.geometry import Point, LineString, Polygon


def createPointGeom(x_coord, y_coord):
    vertex_obj = Point(x_coord, y_coord)
    return vertex_obj


def createLineGeom(vertexlist):
    for points in vertexlist:
        line = LineString([points])

def createPolyGeom(list):
    if type(list) is list == True:
        poly2 = Polygon([[p.x, poly2.y] for p in [list]])
    elif type(list) is tuple == True:
        poly2 = Polygon([[p.x, poly2.y] for p in [list]])

def getCentroid(ShapeObj):
    centroid1 = ShapeObj.centroid
    return centroid1

def getArea(Shapeobj):
    if type(Shapeobj) is LineString == True:
        l_length == line.Shapeobj
    if type(Shapeobj) is Polygon == True:
        p_length == line.Shapeobj
    else:
        print("Error: I've got a doodoo in my butt")

df = pd.read.csv('.txt', sep = ",", header = None)
df.columns = []

def getpoints(dataframe):
    originx = df['from_x']
    originy = df['from_y']
    destinationx = df['to_x']
    destinationy = df['to_y']
    vertex_x = []
    vertex_y = []
    for x in originx:
        vertex_x.append(x)
    for x in destinationx:
        vertex_x.append(x)
    for y in originy:
        vertex_y.append(y)
    for y in destinationy:
        vertex_y.append(y)
    return vertex_x, vertex_y

def createPointGeom(x_coord, y_coord):
    vertex_obj = Point(x_coord, y_coord)
    return vertex_obj
