def decimal_to_base_n(decimal_num: int, base: int) -> str:
    """
    Функция для перевода числа из десятичной системы счисления в систему с основанием base.

    :param decimal_num: Число в десятичной системе счисления.
    :param base: Основание системы счисления, в которую нужно перевести число.
    :return: Число в целевой системе счисления.
    """
    if base < 2 or base > 16:
        raise ValueError("Основание системы счисления должно быть в диапазоне от 2 до 16.")

    if decimal_num == 0:
        return '0'  # Случай, когда исходное число равно нулю

    result = ""
    while decimal_num > 0:
        remainder = decimal_num % base
        result = get_digit(remainder) + result
        decimal_num = decimal_num // base

    return result


def get_digit(remainder: int) -> str:
    """
    Вспомогательная функция для получения символа для остатка при переводе в систему с основанием больше 10.

    :param remainder: Остаток от деления.
    :return: Символ для остатка (A-F для основания больше 10).
    """
    if remainder < 10:
        return str(remainder)
    else:
        return chr(ord('A') + remainder - 10)


def base_n_to_decimal(num: int, base: int):
    """
    Функция для перевода числа из системы с основанием base в десятичную систему счисления.

    :param num: Число в целевой системе счисления.
    :param base: Основание системы счисления числа.
    :return: Число в десятичной системе счисления.
    """
    if base < 2 or base > 16:
        raise ValueError("Основание системы счисления должно быть в диапазоне от 2 до 16.")

    decimal_num = 0
    num = num.upper()  # Приводим символы к верхнему регистру (для шестнадцатеричной системы)
    for digit in num:
        if digit.isnumeric():
            digit_value = int(digit)
        elif 'A' <= digit <= 'F':
            digit_value = ord(digit) - ord('A') + 10
        else:
            raise ValueError("Некорректный символ в числе.")

        if digit_value >= base:
            raise ValueError("Символ в числе превышает основание системы счисления.")

        decimal_num = decimal_num * base + digit_value

    return decimal_num
