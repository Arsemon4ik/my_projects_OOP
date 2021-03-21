from figures import Rectangle, Square, Circle

rect_1 = Rectangle(3,4)
rect_2 = Rectangle(12,5)
#вывод площади наших двух прямоугольников
print(rect_1.get_area_rectangle())
print(rect_2.get_area_rectangle())
print("\n")

square_1 = Square(10)
square_2 = Square(6)


print(square_1.get_area_square(),square_2.get_area_square())
print("\n")


circ_1 = Circle(25)
circ_2 = Circle(11)

print(circ_1.get_area_circle(),circ_2.get_area_circle())
print("\n")

figures = [rect_1,rect_2,square_1,square_2,circ_1,circ_2]

for figure in figures:
    if isinstance(figure,Square):
        print("Square: "+ str(figure.get_area_square()))
    elif isinstance(figure,Rectangle):
        print("Rectangle: " + str(figure.get_area_rectangle()))
    elif isinstance(figure,Circle):
        print("Circle: " + str(figure.get_area_circle()))

