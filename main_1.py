def no_x(name, t, x_d): # t - кол-во букв в родной  планете корабля.
    # Находим Х если х = 0
    n = int(name.split("-")[1][0]) # первая цифра в номере корабля
    if n > 5:
        return n + x_d
    else:
        return (n + x_d) * -4 + t

def no_y(name, t, y_d): # t - кол-во букв в родной  планете корабля.
    # Находим Y если y = 0
    n = int(name.split("-")[1][0]) # первая цифра в номере корабля
    m = int(name.split("-")[1][1]) # вторая цифра в номере корабля
    if m > 3:
        return m + t + y_d
    else:
        return -1 * (n + y_d) * m

file = open('space.txt').readlines()
for i in file:
    i = i.split("*") # массив с параметрами коробля 
    name = i[0] # Код корабля-номер корабля
    planet = [1] # название родной планеты корабля
    coord_x = int(i[2].split(" ")[0]) # x coord_place
    coord_y = int(i[2].split(" ")[1]) # y coord_place
    d_x = int(i[3].split(" ")[0]) # x direction
    d_y = int((i[3].split(" ")[1]).replace("\n", "")) # y direction

    if coord_x == 0: coord_x = no_x(name, len(planet), d_x)
    if coord_y == 0: coord_y = no_x(name, len(planet), d_y)

    code = name.split("-")[0][-1] #  код корабля 

    if "V" == code:
        print(f"{name} - ({coord_x}, {coord_y})")

    #print(f"{name}*{planet}*{coord_x} {coord_y}*{d_x} {d_y}")

    
