import random

def guess_the_number():
    """
    Игра "Угадай число".
    Компьютер загадывает число от 1 до 10, а пользователь пытается его угадать за 3 попытки.
    """

    secret_number = random.randint(1, 10)
    attempts_left = 3

    print("Добро пожаловать в игру 'Угадай число'!")
    print("Я загадал число от 1 до 10.")

    while attempts_left > 0:
        print(f"У вас осталось {attempts_left} попыток.")
        try:
            guess = int(input("Ваше предположение: "))
        except ValueError:
            print("Пожалуйста, введите целое число.")
            continue

        if guess < secret_number:
            print("Слишком мало!")
        elif guess > secret_number:
            print("Слишком много!")
        else:
            print(f"Поздравляю! Вы угадали число {secret_number}!")
            return

        attempts_left -= 1

    print(f"Вы проиграли. Загаданное число было {secret_number}.")

if __name__ == "__main__":
    guess_the_number()