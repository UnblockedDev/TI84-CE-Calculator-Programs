import math

while True:

    type = input("What do you need help with?     (1: Area 2: Pythagorean Theorem  3: SohCahToa  4: Volume) ")

    if type == "1":
        typeA = input("What shape? (1: Circle, 2: Triangle, 3: Polygon) ")

        if typeA == "1":
            radius = float(input("Radius: "))

            print(round(math.pi*(radius**2), 3), "   or   ", round(radius**2, 3), "pi")
        elif typeA == "2":
            base = float(input("Base: "))
            height = float(input("Height: "))

            print(round((base*height)/2, 3))
        elif typeA == "3":
            knowBase = input("Do you know the base? (1: yes   2: no) ")

            if knowBase == "1":
                knowAny = input("Do you know the Apothem? (1: yes   2: no) ")
                sides = float(input("Sides: "))
                deg = (360 / sides) / 2

                if knowAny == "1":
                    base = float(input("Base: "))
                    apothem = float(input("Apothem: "))

                    print(round((apothem * base * sides / 2), 3))
                elif knowAny == "2":
                    base = float(input("Base: "))
                    apothem = (base / 2) / (math.tan(math.radians(deg)))

                    print(round((apothem * base * sides / 2), 3))

            elif knowBase == "2":
                knowAny = input("What do you know: Hypotenuse or Apothem? ")
                sides = float(input("Sides: "))
                deg = (360 / sides) / 2
                if knowAny == "1":
                    hyp = float(input("Hypotenuse: "))
                    apothem = hyp * (math.cos(math.radians(deg)))
                    base = (hyp * (math.sin(math.radians(deg)))) * 2

                    print(round((apothem * base * sides / 2), 3))
                elif knowAny == "2":
                    apothem = float(input("Apothem: "))
                    hyp = apothem / (math.cos(math.radians(deg)))
                    base = (apothem * (math.tan(math.radians(deg)))) * 2

                    print(round((apothem * base * sides / 2), 3))
                else:
                    pass
            else:
                pass
        else:
            pass


    elif type == "2":
        typeP = input("Are you missing a, b, or c? ")

        if typeP == "1":
            bNum = float(input("b: "))
            cNum = float(input("c: "))
            aKinda = cNum**2 - bNum**2

            print(round(math.sqrt(aKinda), 3), "  or   The Squareroot of", round(aKinda, 3))
        elif typeP == "2":
            aNum = float(input("a: "))
            cNum = float(input("c: "))
            bKinda = cNum**2 - aNum**2

            print(round(math.sqrt(bKinda), 3), "  or   The Squareroot of", round(bKinda, 3))
        elif typeP == "3":
            aNum = float(input("a: "))
            bNum = float(input("b: "))
            cKinda = aNum**2 + bNum**2

            print(round(math.sqrt(cKinda), 3), "  or   The Squareroot of", round(cKinda, 3))
        else:
            pass

    elif type == "3":
        typeSCT = input("Sin, Cosine, or Tangent? ")

        if typeSCT == "1":
            typeS = input("What is missing: Angle, Opposite, or Hypotenuse? ")

            if typeS == "1":
                opp = float(input("Opposite: "))
                hyp = float(input("Hypotenuse: "))

                print(round(math.asin(opp / hyp), 3))
            elif typeS == "2":
                ang = float(input("Angle: "))
                hyp = float(input("Hypotenuse: "))

                print(round(math.sin(math.radians(ang)) * hyp, 3))
            elif typeS == "3":
                ang = float(input("Angle: "))
                opp = float(input("Opposite: "))

                print(round(opp / math.sin(math.radians(ang)) , 3))
            else:
                pass


        elif typeSCT == "2":
            typeC = input("What is missing: Angle, Adjacent, or Hypotenuse? ")

            if typeC == "1":
                adj = float(input("Adjacent: "))
                hyp = float(input("Hypotenuse: "))

                print(round(math.acos(adj / hyp), 3))
            elif typeC == "2":
                ang = float(input("Angle: "))
                hyp = float(input("Hypotenuse: "))

                print(round(math.cos(math.radians(ang)) * hyp, 3))
            elif typeC == "3":
                ang = float(input("Angle: "))
                adj = float(input("Adjacent: "))

                print(round(adj / math.tan(math.radians(ang)), 3))
            else:
                pass


        elif typeSCT == "3":
            typeT = input("What is missing: Angle, Opposite, or Adjacent? ")

            if typeT == "1":
                opp = float(input("Opposite: "))
                adj = float(input("Adjacent: "))

                print(round(math.atan(opp / adj), 3))
            elif typeT == "2":
                ang = float(input("Angle: "))
                adj = float(input("Adjacent: "))

                print(round(math.tan(math.radians(ang)) * adj, 3))
            elif typeT == "3":
                ang = float(input("Angle: "))
                opp = float(input("Opposite: "))

                print(round(opp / math.tan(math.radians(ang)), 3))
            else:
                pass
        else:
            pass


    elif type == "4":
        typeV = input('Basic, "Comes to a point", or Sphere? ')

        if typeV == "1":
            base = float(input("Base: "))
            height = float(input("Height: "))

            print(round(base * height, 3))
        elif typeV == "2":
            whatHeight = input("Which do you have: Normal Height, or Slant Height? ")

            if whatHeight == "1":
                base = float(input("Base: "))
                height = float(input("Height: "))

                print(round((base * height) / 3, 3))
            elif whatHeight == "2":
                base = float(input("Base: "))
                radius = float(input("Radius of Base: "))
                slant = float(input("Slant Height: "))

                height = math.sqrt((slant**2) - (radius**2))

                print(round((base * height) / 3, 3))
            else:
                pass

        elif typeV == "3":
            radius = float(input("Radius: "))

            print(round(math.pi*(radius**3) * (4 / 3), 3), "   or    ", round((radius**3) * (4 / 3), 3), "pi")
        else:
            pass
    else:
        pass