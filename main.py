from utils import load_random_word

user_name = input("Введите имя игрока\n")
print(f"Привет, {user_name}!")
print(f"Составьте 8 слов из слова '{load_random_word()}'")
print("Слова должны быть не короче 3 букв")
print("Чтобы закончить игру, угадайте все слова или напишите 'stop'")
user_word = input("Поехали, ваше первое слово?\n")

