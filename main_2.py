def mySort(mas):
    #  сортировка массива со вычислительной сложностью алгоритма — O(n2)
    for i in range(len(mas)):
        _min = i 
        for j in range(i, len(mas)):
            if mas[j] < mas[_min]: _min = j
        temp = mas[i]
        mas[i] = mas[_min]
        mas[_min] = temp
    return mas




list = {} # словарь номер-код
mas = []  # Массив с номерами
file = open('space.txt').readlines()
for i in file:
    i = i.split("*") # массив с параметрами коробля 
    name = (i[0].split("-"))[0] # Код корабля
    code = (i[0].split("-"))[1] # номер корабля
    list[code] = name 
    mas.append(int(code))

mas = mySort(mas)

for i in range(10):
    print(f"{list[str(mas[i])]}-{mas[i]}")