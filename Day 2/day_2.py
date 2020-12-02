import re

def day_2_puzzle_1():
    #open file and read data
    with open("day_2_puzzle_1.txt", "r+") as f:
        line_data = [line.strip() for line in f]

    valid_passwords = 0
    for line in line_data:
        pw_constraint_split = re.split('-| |:',line) 
        min_num = int(pw_constraint_split[0]) 
        max_num = int(pw_constraint_split[1]) 
        letter = pw_constraint_split[2] 
        password = pw_constraint_split[4]


        if password.count(letter) >= min_num and password.count(letter) <= max_num:
                valid_passwords += 1

    print(valid_passwords)


def day_2_puzzle_2():
        #open file and read data
    with open("day_2_puzzle_1.txt", "r+") as f:
        line_data = [line.strip() for line in f]

    valid_passwords = 0
    for line in line_data:
        pw_constraint_split = re.split('-| |:',line) 
        first_idx = int(pw_constraint_split[0]) - 1
        second_idx = int(pw_constraint_split[1]) - 1
        letter = pw_constraint_split[2] 
        password = pw_constraint_split[4]


        if (password[first_idx] == letter) ^ (password[second_idx] == letter):
            valid_passwords += 1

    print(valid_passwords)
    

def main():
    day_2_puzzle_1()
    day_2_puzzle_2()

main()