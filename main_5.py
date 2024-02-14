list = {} # словарь название планета - остальные параметры
file = open('space.txt').readlines()
for i in file:
    i = i.split("*") # массив с параметрами коробля 
    name = i[0] # Код корабля-номер корабля
    planet = i[1] # название родной планеты корабля
    coord_x = int(i[2].split(" ")[0]) # x coord_place
    coord_y = int(i[2].split(" ")[1]) # y coord_place
    d_x = int(i[3].split(" ")[0]) # x direction
    d_y = int((i[3].split(" ")[1]).replace("\n", "")) # y direction
    

    if planet in list:
        temp = list[planet]
        temp.append(f"Корабль {name} был отправлен с планеты: {planet} и его направление движения было: {d_x} {d_y}") # Какую инфу выводить вы не сказали
        list[planet] = temp
    else:
        list[planet] = [f"Корабль {name} был отправлен с планеты: {planet} и его направление движения было: {d_x} {d_y}"]
def shipFrom(Q_planet):
    # Функция, которая выводит на экран инф о корабле в формате: Корабль <ShipName> был отправлен с планеты: <planet> и его направление движения было: <direction>
    # Q - планета
        for planet in list[Q_planet]:
            print(*planet)

Q = input()
while Q != "stop":
    if Q in list:
        shipFrom(Q)
    else:
        print("error.. er.. ror..")
    Q = input()