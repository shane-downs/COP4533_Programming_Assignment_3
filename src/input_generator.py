import random
import string

input_size = random.randint(25, 30)

for file_num in range(1, 11):
    with open(f'input_{file_num}.in', 'w') as f:
        letter1 = ""
        letter2 = ""
        value_dict = {}
        chosen_numbers = []
        a_size = random.randint(25, 50)
        b_size = random.randint(25, 50)
        for i in range(a_size):
            letter1 += random.choice(string.ascii_lowercase)
            if letter1[-1] not in value_dict:
                value = random.randint(1, input_size)
                if len(value_dict) == 0:
                    value_dict[letter1[-1]] = value
                else:
                    while value != chosen_numbers[-1]:
                     value = random.randint(1, input_size)
                chosen_numbers.append(value)
                value_dict[letter1[-1]] = value
        for j in range(b_size):
            letter2 += random.choice(string.ascii_lowercase)
            if letter2[-1] not in value_dict:
                value = random.randint(1, input_size)
                if len(value_dict) == 0:
                    value_dict[letter2[-1]] = value
                else:
                    while value != chosen_numbers[-1]:
                        value = random.randint(1, input_size)
                chosen_numbers.append(value)
                value_dict[letter2[-1]] = value

        f.write(str(len(value_dict))+"\n")
        for key, value in value_dict.items():
            f.write(f"{key} {value}\n")
        f.write(letter1+"\n")
        f.write(letter2+"\n")

        f.close()

