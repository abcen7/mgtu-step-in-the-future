from utils import system_numbers

N = int(input())

number_to_fourth_base = system_numbers.decimal_to_base_n(N, 4)

print(list(str(number_to_fourth_base)).count("3"))

