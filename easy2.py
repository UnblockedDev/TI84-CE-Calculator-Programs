import math

while True:

    type = input("What do you need help with?     (1: Surface Area) ")


    if type == "1":
        typeSA = input("Cube, Cylinder, Cone, Sphere,   Triangular Prisim, Pyramid? ")

        if typeSA == "1":
            edge = float(input("Any Edge: "))

            print(round(6 * (edge**2), 3))
        elif typeSA == "2":
            radius = float(input("Radius: "))
            height = float(input("Height: "))

            print(round((2 * math.pi * radius) * (radius + height), 3), "   or    ", round((2 * radius) * (radius + height), 3), "pi")
        elif typeSA == "3":
            whatHeight = input("Which do you have: Normal Heightor Slant Height? ")

            if whatHeight == "1":
                radius = float(input("Radius: "))
                height = float(input("Height: "))

                slant = math.sqrt((height ** 2) + (radius ** 2))

                print(round(math.pi * radius * (radius + slant), 3), "   or    ", round(radius * (radius + slant), 3), "pi")
            elif whatHeight == "2":
                radius = float(input("Radius: "))
                slant = float(input("Slant Height: "))

                print(round(math.pi * radius * (radius + slant), 3), "   or    ", round(radius * (radius + slant), 3), "pi")
            else:
                pass
        elif typeSA == "4":
            radius = float(input("Radius: "))

            print(round(4 * math.pi * (radius**2), 3), "   or    ", round(4 * (radius**2), 3), "pi")
        elif typeSA == "5":
            # easy = input("Does it give you the triangle's height or just the slant heights? ")
            #
            # if easy == "1":
            #     bottom = float(input("Bottom Length of Triangle: "))
            #     height = float(input("Height of Triangle: "))
            #     length = float(input("Length of Prism: "))
            #
            #     slant1 = math.sqrt(height**2 + (bottom / 2)**2)
            #     slant2 = math.sqrt(height**2 + (bottom / 2)**2)

            bottom = float(input("Bottom Length of Triangle: "))
            slant1 = float(input("Slant Height 1: "))
            slant2 = float(input("Slant Height 2: "))
            height = float(input("Height of Triangle: "))
            length = float(input("Length of Prism: "))

            print(round((slant1 + slant2 + bottom) * length + (bottom * height), 3))
        elif typeSA == "6":
            whatHeight = input("Which do you have: Normal Heightor Slant Height? ")

            if whatHeight == "1":
                radius = float(input("Radius of Base (From One Point  to the Middle): "))
                base = float(input("Base: "))
                perimeter = float(input("Perimeter of Base: "))
                height = float(input("Height: "))

                slant = math.sqrt((height**2) + (radius**2))

                print(round((0.5 * perimeter * slant) + base, 3))
            elif whatHeight == "2":
                base = float(input("Base: "))
                perimeter = float(input("Perimeter of Base: "))
                slant = float(input("Slant Height: "))

                print(round((0.5 * perimeter * slant) + base, 3))
            else:
                pass

        else:
            pass
    else:
        pass