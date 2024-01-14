# Создайте класс `BasicWord` в отдельном файле. Этот класс будет содержать в себе:
# **Поля:**
# - исходное слово,
# - набор допустимых подслов.
# **Методы:**
# - проверку введенного слова в списке допустимых подслов (вернет bool),
# - подсчет количества подслов (вернет int).
# Не забудьте определить метод  `__repr__`
#
# **При инициализации** экземпляру задаются: **исходное слово** и набор **допустимых слов,** составленных из исходного. ****
word_count = 0
class Basic_word:
    def __init__(self, word, subwords):
        self.word = word
        self.subwords = subwords
    def is_word_in_subwords(self, user_word, subwords):
        if user_word in subwords:
            return True
        else:
            return False

    def subwords_amount(self):
        if user_word in subwords:
            word_count += 1

word = Basic_word()
word.is_word_in_subwords()
word.subwords_amount()