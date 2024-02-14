list = {} # словарь название коробля - остальные параметры
file = open('space.txt').readlines()
for i in file:
    i = i.split("*") # массив с параметрами коробля 
    name = i[0] # Код корабля-номер корабля
    planet = i[1] # название родной планеты корабля
    coord_x = int(i[2].split(" ")[0]) # x coord_place
    coord_y = int(i[2].split(" ")[1]) # y coord_place
    d_x = int(i[3].split(" ")[0]) # x direction
    d_y = int((i[3].split(" ")[1]).replace("\n", "")) # y direction
    list[name] = (planet, coord_x, coord_y, d_x, d_y)

Q = input() # Запрос пользователя
while Q != "stop":
    if Q in list:
        print(f"Корабль {Q} был отправлен с планеты: {list[Q][0]} и его направление движения было: {list[Q][3]} {list[Q][4]}")
    else:
        print("error.. er.. ror..")
    Q = input()
