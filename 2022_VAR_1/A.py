N = int(input())

N_to_list = list(map(int, list(str(N))))

min_digit_in_number = min(N_to_list)

for index, x in enumerate(N_to_list):
    if x == min_digit_in_number:
        N_to_list[index] = min_digit_in_number + 2

new_number = int("".join(list(map(str, N_to_list))))
print(abs(new_number - N))
