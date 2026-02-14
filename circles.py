pi = float(3.14159265359)
isloop = True

# Gets the angle of the arc from the user
def angleIn():
    angle = input("Arc angle \33[1;33m(0 for whole)\33[0m:\n")
    angle = float(angle)
    if angle == 0:
        angle = 360
    return angle

# Calculates the circumference of a circle or arc
def circumferenceCalculation(israd,measurement):
    angle = angleIn()

    if israd:
        measurement *= 2
        ans = (measurement * pi)*(angle/360)
    else:
        ans = (measurement * pi)*(angle/360)

    return ans

# Calculates the area of a circle or arc
def areaCalculation(israd,measurement):
    angle = angleIn()

    if israd:
        measurement *= measurement
        ans = (measurement * pi)*(angle/360)

    else:
        measurement = measurement/2
        measurement *= measurement
        ans = (measurement * pi)*(angle/360)

    return ans

# Calculates the volume of a cylinder, with the addition of a request of the length of the cylinder
def volumeCalculation(israd,measurement):
    length = float(input("length of cylinder: "))

    if israd:
        measurement *= measurement
        ans = (measurement * pi)*length

    else:
        measurement = measurement/2
        measurement *= measurement
        ans = (measurement * pi)*length

    return ans

# Asks for either a radius or perimeter
def Radius_or_Diameter_Meaasurements():
    selection = []
    ans = input("\33[1;3;4m///Measurement///\33[0m\nRadius \033[1;33m(r)\033[0m \nDiameter \033[1;33m(d)\033[0m\n")

    if ans  == "r":
        measurement = input("Enter radius:")
        measurement = float(measurement)
    elif ans == "d":
        measurement = input("Enter diameter:")
        measurement = float(measurement)
    else:
        return 0

    selection.append(ans)
    selection.append(measurement)
    return selection

# Asks for a selection between calculating the Circumference, Area or Volume
def circumference_Area_Volume_Calculation(selection:list) -> list | int:
    if type(selection) == int:
        print("Please enter either radius or perimeter")
        return
    
    ans =input("\33[1;3;4m///Calculation///\33[0m\nCircumfrence \033[1;33m(c)\033[0m \nArea \033[1;33m(a)\033[0m \nVolume \033[1;33m(v)\033[0m \n")
    RorP = selection[0]
    measurement = selection[1]

    match RorP:
        case "r":
            israd = True
        case "p":
            israd = False

    match ans:
        case "c":
            out = circumferenceCalculation(israd,measurement)
        case "a":
            out = areaCalculation(israd,measurement)
        case "v":
            out = volumeCalculation(israd,measurement)
        case _:
            print("Invalid choice")
            return
        
    print("Result is:")
    print(out)

# Code execution
while isloop:

    radius_or_Diameter = Radius_or_Perimeter_Meaasurements()

    circumference_Area_Volume_Calculation(radius_or_Diameter)
             
    print("\n\n press Enter to proceed; 'exit' to quit")
    if input() == "exit":
        exit()
