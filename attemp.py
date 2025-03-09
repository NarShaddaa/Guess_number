
def find_max_odd_number(numbers: list[int]) -> int:
    """
    Ищет максимальное чётное значение в списке положительных целых значений,
    переданном в параметр функции.
    """
    Current_Max = 0
    for number in numbers:
        if number % 2 == 0:
            Current_Max = max(number, Current_Max)
    return Current_Max


max_odd = find_max_odd_number([10, 8, 6, 4, 2])
# Попробуйте передать в find_max_odd_number() другие списки:
print(f'Максимальное чётное число: {max_odd}')
