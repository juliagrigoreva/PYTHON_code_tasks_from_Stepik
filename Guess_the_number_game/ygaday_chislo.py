import random

x = random.randint(1, 100)
easy = "изи (неограниченное число попыток и подсказки 'больше-меньше')"
middle = "мидл (7 попыток и подсказки 'больше-меньше')"
hard = "хард (не больше 7 попыток и без подсказок)"
counter = 0
too_much = [
    "Многовато! Моё число меньше твоего",
    "Перелёт! Твой прицел сбился вверх, бери ниже",
    "Ого, ты замахнулся! Моё число скромнее",
    "Перебор. Попробуй уменьшить значение",
    "Планка поднята слишком высоко. Спускайся пониже!",
    "Это число выше моей цели. Давай еще раз",
    "Хватил лишнего! Убавь немного",
    "Ту мач...",
    "Нужно число поменьше",
    "Ух, как много! Моё число меньше",
]
not_enough = [
    "Маловато будет! Загаданное число больше",
    "Недолёт! Число больше",
    "Мелко плаваешь! Моё число больще твоего",
    "Недостаточно. Попробуй увеличить ставку",
    "Твоё число слишком маленькое, дай ему подрасти!",
    "Это ниже цели. Нужно значение покрупнее",
    "Слишком скромно. Добавь-ка еще",
    "Еще недостаточно",
    "Введенное число ниже искомого значения",
    "Попробуй что-то побольше",
]
win = [
    "В точку! Ты угадал именно то число, которое я задумал",
    "Бинго! Это правильный ответ!",
    "В яблочко! Прямое попадание в цель",
    "Невероятно! Твоя интуиция на высоте!",
    "Победа! Число разгадано",
    "Наконец-то! Угадал! Я уже начал думать, что мы тут до завтра застрянем",
    "Ты настоящий гроссмейстер чисел! Абсолютно верно",
    "Джекпот! Ты раскусил мой алгоритм",
    "Ура! У тебя получилось! Это было непросто, но ты справился",
    "Ты читаешь мои мысли? Это именно то самое число!",
]


def is_valid(y):  # проверка на дурака (число)
    return y > 0 and y < 101


def valid_level(level):  # проверка на дурака (уровень)
    return 0 < level < 4


def level_is(level):  # выбор уровня сложности
    if level == 1:
        return f"Твой уровень: {easy}"
    elif level == 2:
        return f"Отлично, риск ни к чему. Твой уровень: {middle}"
    elif level == 3:
        return f"Ого, ты смелый! Твой уровень: {hard}"


def igra():
    print(f"{name}, я загадал число от 1 до 100. Угадаешь?")
    print()
    print(
        f"{name}, для начала выбери уровень сложности: \n 1 - {easy}  \n 2 - {middle}  \n 3 - {hard}"
    )  # пользователь выбирает уровень сложности
    print()
    level = int(input())
    if valid_level(level) == False:
        while valid_level(level) == False:
            print("{name}, 1, 2 или 3 - все просто. Напиши нужную цифру")
            level = int(input())
    print()
    print(level_is(level))
    print()

    if level == 1:  # вариант игры уровень 1
        print(f"{name}, жду твой ход")
        step_polz = int(input())
        print()
        if is_valid(step_polz) == False:
            while is_valid(step_polz) == False:
                print(f"{name}, прочти ка инструкцию еще раз. Число от 0 до 100")
                step_polz = int(input())
        while step_polz != x:
            if step_polz > x:
                print(random.choice(too_much))
            elif step_polz < x:
                print(random.choice(not_enough))
            step_polz = int(input())
            print()
        if step_polz == x:
            print(random.choice(win))

    if level == 2:  # вариант игры уровень 2
        counter = 7
        print(f"{name},у тебя {counter} попыток")
        print("Жду твой ход")
        print()
        step_polz = int(input())
        print()
        if is_valid(step_polz) == False:
            while is_valid(step_polz) == False:
                print(f"{name}, прочти-ка инструкцию еще раз. Мое число от 0 до 100")
                step_polz = int(input())
                print()
        while step_polz != x:
            if step_polz > x:
                print(random.choice(too_much))
            elif step_polz < x:
                print(random.choice(not_enough))
            counter -= 1
            print(f"У тебя {counter} попыток")
            print()
            if counter == 0:
                print()
                print(f"{name}, ты не угадал, моё число было {x}")
                break
            step_polz = int(input())
            print()
        if step_polz == x:
            print(random.choice(win))

    if level == 3:  # вариант игры уровень 3
        counter = 7
        print(f"{name}, тебя {counter} попыток")
        print()
        print("Жду твой ход")
        step_polz = int(input())
        print()
        if is_valid(step_polz) == False:
            while is_valid(step_polz) == False:
                print(f"{name}, прочти ка инструкцию еще раз. Число от 0 до 100")
                step_polz = int(input())
        while step_polz != x:
            counter -= 1
            print(f"Не угадал, пробуй еще раз. У тебя {counter} попыток")
            if counter == 0:
                print()
                print(f"{name}, ты не угадал, моё число было {x}")
                break
            step_polz = int(input())
            print()
        if step_polz == x:
            print(random.choice(win))

    print()
    print()
    print(f"{name}, сыграем еще? Напиши 'да' или 'нет'")
    choice = input()
    while choice == "да":
        igra()
    if choice == "нет":
        print(f"{name}, спасибо за игру")


print()
print("Приветствую тебя в Числовой Угадайке. Как я могу к тебе обращаться?")
name = input()
print()
igra()
