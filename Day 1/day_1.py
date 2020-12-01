"""
AoC Day 1 Puzzle 1
Author: Hasnain Cheena
Date: 1/12/2020
"""

def day_1_part_1():
    #open file and read data
    with open("data.txt", "r+") as work_data:
        line_data = work_data.readlines()
        
    #convert str to int 
    expenses = [int(line.strip("\n")) for line in line_data]

    #find two entries that sum to 2020
    idx = 0
    result_found = False
    while not(result_found):
        expense_pair_1 = expenses[idx]
        expenses.pop(idx)
        for expense_pair_2 in expenses:
            if expense_pair_1 + expense_pair_2 == 2020:
                product = expense_pair_1 * expense_pair_2
                result_found = True

    print(product)

def day_1_part_2():
    #open file and read data
    with open("test_data.txt", "r+") as work_data:
        line_data = work_data.readlines()

    #convert str to int 
    expenses = [int(line.strip("\n")) for line in line_data]

    #find three entries that sum to 2020
    result_found = False
    while not(result_found):
        

def main():
    day_1_part_1()
    day_1_part_2()

main()