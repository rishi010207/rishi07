#FYCS_54 Shape Class Demo

class shapes:

    def __init__(self,square,rectangleLength,rectangleBreadth):
        #Shape Declaration.
        self.square=square
        self.rectangleLength=rectangleLength #Length
        self.rectangleBreadth=rectangleBreadth #Breadth

        #Calculations.
        self.areaSquare=square ** 2
        self.areaRectangle=rectangleLength * rectangleBreadth
        self.perimeterSquare=square * 4
        self.perimeterRectangle=2 * rectangleLength * rectangleBreadth

    def display(self):
        #Display function
        print("Side of a Square: ", self.square)
        print("Area of Square: ",self.areaSquare)
        print("Perimeter of Square: ", self.perimeterSquare)
        print("Length of the Rectangle: ", self.rectangleLength)
        print("Breadth of the Rectangle: ", self.rectangleBreadth)
        print("Area of Rectangle: ", self.areaRectangle)
        print("Perimeter of Rectangle: ", self.perimeterRectangle)

#User Input
square = int(input("Please enter the Square's Size: "))
rectangleLength=int(input("Please enter the Length of Rectangle: "))
rectangleBreadth=int(input("Please enter the Breadth of Rectangle: "))
#Output
SI = shapes(square,rectangleLength,rectangleBreadth)
SI.display()
