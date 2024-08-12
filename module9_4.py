first = 'Мама мыла раму'
second = 'Рамена мало было'

result = list(map(lambda x, y: x == y, first, second))

print(result)


def get_advanced_writer(file_name):
    def write_everything(*data_set):
        with open(file_name, 'a', encoding='utf-8') as i:
            for item in data_set:
                i.write(f'{item}\n')

    return write_everything


write = get_advanced_writer('example.txt')
write('Это строчка', ['А', 'это', 'уже', 'число', 5, 'в', 'списке'])

from random import choice


class MysticBall:
    def __init__(self, *words):
        self.words = words

    def __call__(self):
        return choice(self.words)


# Пример использования
first_ball = MysticBall('Да', 'Нет', 'Наверное', 'Pochemy', 'Zachem', 'Kto')
print(first_ball())
print(first_ball())
print(first_ball())
print(first_ball())