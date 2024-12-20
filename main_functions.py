from functions_for_work import TextProcessor

class MenuFacade:
    def __init__(self):
        self.text_processor = TextProcessor()
        self.array_palindromes = []
        self.is_text_input = False
        self.is_algorithm_done = False

    def run(self):
        while True:
            print("Выберите пункт меню:\n"
                  "1. Ввод исходного текста \n"
                  "2. Выполнение алгоритма по поиску палиндромов в тексте\n"
                  "3. Вывод результата\n"
                  "4. Выход из цикла")
            choice = input()
            if self.text_processor.is_int(choice):
                choice = int(choice)

            if choice == 1:
                self.is_text_input = self.text_processor.input_text()
            elif choice == 2:
                if self.is_text_input:
                    self.array_palindromes = self.text_processor.find_palindromes()
                    self.is_algorithm_done = True
                else:
                    print("Ошибка!\nСначала введите текст\n\n")
            elif choice == 3:
                if self.is_algorithm_done:
                    if self.is_text_input:
                        self.text_processor.print_palindromes(self.array_palindromes)
                else:
                    print("\nСначала выполните алгоритм\n")
            elif choice == 4:
                break
            else:
                print('error')