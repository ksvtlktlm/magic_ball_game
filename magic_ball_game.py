import random


def continue_game():
    while True:
        print()
        print('Хочешь спросить еще что-нибудь? "д" - да, "н" - нет...')
        ans = input()
        if ans == 'д' or ans == 'l':
            game()
            break
        if ans == 'н' or ans == 'y':
            print('Возвращайся, если возникнут вопросы!')
            break


def choice(answers):
    num = random.randint(0, 19)
    answer = answers[num]
    return answer


def game():

    answers = ["Бесспорно", "Мне кажется - да", "Пока неясно, попробуй снова",  "Даже не думай",

    "Предрешено",   "Вероятнее всего",  "Спроси позже", "Мой ответ - нет",

    "Никаких сомнений", "Хорошие перспективы",  "Лучше не рассказывать",    "По моим данным - нет",

    "Определённо да",   "Знаки говорят - да",   "Сейчас нельзя предсказать",    "Перспективы не очень хорошие",

    "Можешь быть уверен в этом",    "Да",   "Сконцентрируйся и спроси опять",   "Весьма сомнительно"]

    print('Привет Мир, я магический шар, и я знаю ответ на любой твой вопрос.')
    name = input('Введи свое имя: ')
    print(f'Привет, {name}!')
    while True:
        print('Задай свой вопрос: ')
        input()
        res = choice(answers)
        print(res)
        continue_game()
        break


game()