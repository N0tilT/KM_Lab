
import SMO as s

def PrintMenu():
    print("*******************")
    print("Меню")
    print("1.Типовые задачи")
    print("2.Своя задача")
    print("0.Выход")

def PrintTask():
    print("*******************")
    print("Задачи")
    print("1.Задача 1: Одноканальная СМО с отказами. ")
    print("2.Своя задача")
    print("0.Выход")

choice=3
while choice!=0:
    PrintMenu()
    i=s.SMO.factorial(4)
    print(i)
    choice=int(input())
    match choice:
        case 1:
            PrintTask()
        case 2:
            print("Интенсивность потока:")
            lamb=float(input())
            print("Время обслуживания:")
            time=float(input())
            print("Количество линий обслуживания:")
            channel_count=int(input())
            print("Очередь ...")
            print("1.С отказами")
            print("2.Неограниченная")
            print("3.Ограниченная")
            type_queue=int(input())
        case _:
            print("Введите цифру, которая будет соответствовать выбранному вами пункту")
            continue