#CSE 107, Prelab 2, Exercise 3.1 Annika Davenport and Donovan Griego
shape = input("Please enter a shape: ")

if shape == "circle":
    radius = float(input("Please enter a radius: "))
    circ = 2 * 3.14 * radius
    area = 3.14 * radius**2
    print("The circumference of the circle is\n" + str(circ))
    print("The area of the circle is\n" + str(area))
  #Block that prints area and circumference should user choose circle.
elif shape == "rectangle":
    width = float(input("Please enter a width for the rectangle: "))
    length = float(input("Please enter a length for the rectangle: "))
    peri = (2 * width) + (2 * length)
    area = width * length
    print("The perimeter of the rectangle is\n" + str(peri))
    print("The area of the rectangle is\n" + str(area))
    #Block that prints perimeter and area of a rectangle should user choose rectangle.
elif shape == "square":
    length = float(input("Please enter a side length for the square: "))
    peri = 4 * length
    area = length**2
    print("The perimeter of the square is\n" + str(peri))
    print("The area of the square is\n" + str(area))
    #Block that prints perimeter and area of a square should user choose square.
else:
    print("Enter a valid shape")