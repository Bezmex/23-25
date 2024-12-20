import random
import re

class TextProcessor:
    def __init__(self):
        self.message = ""

    def is_int(self, choice):
        try:
            if type(choice) is int:
                return True
            if choice is None:
                return False
            if not choice.isdecimal():
                return False
            int(choice)
            return True
        except (Exception, ValueError, TypeError):
            return False

    def input_text(self):
        print("Выберите тип ввода:\n1. Ввод текста с клавиатуры\n2. Случайная генерация")
        type_input = input()

        if self.is_int(type_input):
            type_input = int(type_input)
        if type_input == 1:
            self.message = self._input_text_from_keyboard()
            print(f"Вы ввели следующий текст: {self.message} ")
        elif type_input == 2:
            self.message = self._generate_random_text()
            print(f"Сгенерированный текст: {self.message}")
        else:
            print('error')
        return True

    def _input_text_from_keyboard(self):
        text = input("Введите текст для обработки (для завершения ввода нажмите клавишу Enter): ")
        while True:
            line = input()
            if line == "":
                break
            text += line
        return text

    def _generate_random_text(self):
        letters = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюяАБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ ' + ' ' * 7
        length = random.randint(20, 100)  # Генерация случайной длины
        return ''.join(random.choice(letters) for _ in range(length))

    def find_palindromes(self):
        text = self.message.lower()
        text = re.sub(r'[^\w\s]', '', text)

        words = text.split()

        palindromes = []

        # Проверка слова на палиндром
        for word in words:
            if word == word[::-1]:
                palindromes.append(word)
        print("Алгоритм выполнен\n")
        return palindromes

    def print_palindromes(self, palindromes):
        if len(palindromes) == 0:
            print("Палиндромов в тексте нет")
        else:
            print("Список палиндромов: ")
            for i in palindromes:
                print(i)