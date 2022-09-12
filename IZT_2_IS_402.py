def main():

    try:
        a = int(input('Введите A: '))
        b = int(input('Введите B: '))
        x = int(input('Введите X: '))

        if x < 7:
            y = ((x ** 2) + (a ** 2) + (b ** 2)) / (a + b)
        else:
            y = (x ** 3) * ((a + b) ** 2)

        print("y = %.1f" % y)
    except ValueError:
        print("Ошибка: Данные введены неверно!")
    except ZeroDivisionError:
        print("Ошибка: Деление на ноль!")

    input("Нажмите Enter")

if __name__ == '__main__':
    main()