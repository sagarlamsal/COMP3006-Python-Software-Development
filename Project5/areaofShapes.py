#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 10 15:06:53 2021

@author: sagarlamsal
"""

# Sagar Lamsal

# Shape Classes




import math

class Shape(object):
    def name(self, shape):
        print ("The shape of the object is: %s" %shape)
    
    def __init__ (self, length, height):
        self.length = length        #creating the universal length variable
        self.height = height        #creating the universal width variable

#creating the universal length and width variables means that we can just...
#... call the varibales for the shapes where they are needed. This also means...
#... we won't have to create different length and width for every shape that needs it.

class Rectangle(Shape):
    
        
    def area(self):
        return self.length*self.height
    
    
   
class Oval(Shape):
    def __init__(self, lradius, sradius):
        self.lradius = lradius
        self.sradius = sradius
        
    def area(self):
        return math.pi * self.lradius * self.sradius
    
    
#This is a Regular Polygon
class Polygon(Shape):
    def __init__ (self, n, a,  s):
        self.n = n      #number of sides
        self.a = a      #apothem size
        self.s = s      #length of one side of polygon
        
    def area(self):
        return (1/2) * self.n * self.a * self.s
    
    
    
class Square(Shape):
    def __init__ (self, sides):
        self.sides = sides

        
        
    def area(self):
        return self.sides**2
    
    
    
class Triangle(Shape):

    def area(self):
        return (1/2) * self.length * self.height
    
    
    
    
    
class Pentagon(Shape):
    def __init__(self, n, side, apothem):
        self.side = side      #length of any one side
        self.apothem = apothem
        self.n = n          #number of sides
    
    def area(self):
        area = (1/2) * self.n *self.side * self.apothem
        return area
    

   
class Circle(Shape):
        def __init__(self,radius):
            self.radius = radius
        
        def area(self):
            return math.pi*self.radius*self.radius
        
        
        
      
class Parallelogram(Shape):
    
    def area(self):
        return self.length * self.height




class Rhombus(Shape):
    def __init__(self, aDiameter, bDiameter):
        self.aDiameter = aDiameter
        self.bDiameter = bDiameter
        
    def area(self):
        return (1/2) * self.aDiameter * self.bDiameter


def main():
    r = Rectangle(2,10)
    o = Oval(2,3)
    p = Polygon(6, 4, 4)
    s = Square(6)
    t = Triangle(5, 9)
    pen = Pentagon(5, 4, 6)
    c = Circle(9)
    par = Parallelogram(9, 3)
    rhom = Rhombus(6,4)
    print(f"Area of Rectangle is {r.area()}")
    print(f"Area of Oval is {o.area()}")
    print(f"Area of Polygon is {p.area()}")
    print(f"Area of Square is {s.area()}")
    print(f"Area of Triangle is {t.area()}")
    print(f"Area of Pentagon is {pen.area()}")
    print(f"Area of Circle is {c.area()}")
    print(f"Area of Parallelogram is {par.area()}")
    print(f"Area of Rhombus is {rhom.area()}")




if __name__ =='__main__':
    main()