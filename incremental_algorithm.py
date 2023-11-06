import numpy as np
import matplotlib.pyplot as plt

class Point:
    def __init__(self, x:int , y:int):
        self.x = x
        self.y = y
        
class Plot:
    def __init__(self, y:int, x:int, points:list):
        self.y = y
        self.x = x
        self.points = points
        self.coord = plt.figure()
        self.ax = self.coord.add_subplot(111)
        self.createPlot()
        self.addPoints()
        self.sortPoints()
    
    def createPlot(self):
        self.ax.set_xlim(0, self.x)
        self.ax.set_ylim(0, self.y)
        self.ax.set_xticks([])
        self.ax.set_yticks([])
        
    def addPoints(self):
        for p in self.points:
            self.ax.plot(p.x, p.y, 'go')
    
    def sortPoints(self):
        # Sorting the points by x-value
        # if same x-value by y-value
        self.points.sort(key=lambda p: (p.x, p.y))
    
    def drawLine(self, p1:Point, p2:Point):
        self.ax.plot([p1.x,p2.x], [p1.y, p2.y], 'ro-')
        
    def calculateDeterminant(self, p:Point, p1:Point, p2:Point):
        # p is the point that is checked, p1 and p2 are the points of the line
        n_array = np.array([[1, p1.x, p1.y], 
                            [1, p2.x, p2.y], 
                            [1, p.x, p.y]]) 
        determinant = np.linalg.det(n_array)
        return determinant
        
    def createHull(self, pts:list):
        hull = []
        for i,p in enumerate(pts):
            if i == 0:
                hull.append(p)
                continue
            if i == 1:
                hull.append(p)
                continue
            while len(hull) >= 2:
                if self.calculateDeterminant(p, hull[-2], hull[-1]) > 0:
                    hull.pop()
                else:
                    break
            hull.append(p)
        for i,p in enumerate(hull):
            if i != 0:
                self.drawLine(p, hull[i-1])
                     
    def showPlot(self):
        self.createHull(self.points) # Upper hull
        self.createHull(reversed(self.points)) # Lower hull
        plt.title("Incremental algorithm to find the convex hull")
        plt.show()     
        
if __name__ == "__main__":
    MAX_X = 30
    MAX_Y = 30
    NUM_POINTS = 20
    
    points = []
    for i in range(0, NUM_POINTS):
        new_point = Point(x=np.random.randint(1, MAX_X-1), 
                   y=np.random.randint(1, MAX_Y-1))
        if new_point in points:
            NUM_POINTS += 1
            continue
        points.append(new_point)
    
    plot = Plot(x=MAX_X, y=MAX_Y, points=points)
    plot.showPlot()
    