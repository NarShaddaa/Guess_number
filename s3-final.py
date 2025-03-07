class CipherMaster:
    # Не изменяйте и не перемещайте эту переменную
    alphabet = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'

    def process_text(self, text, shift, is_encrypt):
        # Метод должен возвращать зашифрованный текст
        # с учетом переданного смещения shift.
        result = []
        for letter in text:
            if is_encrypt is True:
                if letter.lower() in self.alphabet:  # здесь ваш код
                    index = self.alphabet.find(letter.lower())
                    new_index = (index + shift) % len(self.alphabet)
                    new_letter = self.alphabet[new_index]
                    result.append(new_letter)
                else:
                    result.append(letter)
            if is_encrypt is False:
                if letter.lower() in self.alphabet:  # здесь ваш код
                    index = self.alphabet.find(letter.lower())
                    new_index = (index - shift) % len(self.alphabet)
                    new_letter = self.alphabet[new_index]
                    result.append(new_letter)
                else:
                    result.append(letter)
        return ''.join(result)


cipher_master = CipherMaster()
print(cipher_master.process_text(
    text='Однажды ревьюер принял проект с первого раза, с тех пор я его боюсь',
    shift=2,
    is_encrypt=True
))
print(cipher_master.process_text(
    text='Олебэи яфвнэ мроплж сэжи — э пэй рдв злййвкпш лп нвящывнэ',
    shift=-3,
    is_encrypt=False
))
