print("password")
file = open('space.txt').readlines()
for i in file:
    i = i.split("*") # массив с параметрами коробля 
    name = i[0] # Код корабля-номер корабля
    code = name.split("-")[0] # Код корабля
    num = name.split("-")[1] # номер корабля
    planet = i[1] # название родной планеты корабля
    coord_x = int(i[2].split(" ")[0]) # x coord_place
    coord_y = int(i[2].split(" ")[1]) # y coord_place
    d_x = int(i[3].split(" ")[0]) # x direction
    d_y = int((i[3].split(" ")[1]).replace("\n", "")) # y direction

    net = planet[-3:] # последние последние 3 буквы планеты
    od = code[1:3][::-1] # перевернутые центральные буквы корабля
    alp = planet[0:3][::-1] # последние первые перевернутые 3 буквы планеты

    print((net + od + alp).upper())