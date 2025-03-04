class Employee:
    # Вместо инструкции pass напишите свой код.
    vacation_days = 28

    def __init__(self, first_name, second_name, gender):
        self.first_name = first_name
        self.second_name = second_name
        self.gender = gender


# Создайте экземпляры класса Employee с различными значениями атрибутов.
employee1 = Employee('прошивка', 'Бешеная', 'ж')
employee2 = Employee('Злой', 'Garret', 'м')

# Допишите код для вывода информации о сотрудниках.
print(f'Имя: {employee1.first_name}, '
      f'Фамилия: {employee1.second_name}, '
      f'пол: {employee1.gender}, '
      f'{employee1.vacation_days}')

print(f'Имя: {employee2.first_name}, '
      f'Фамилия: {employee2.second_name}, '
      f'пол: {employee2.gender}, '
      f'{employee2.vacation_days}')
