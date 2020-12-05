import numpy as np

#@Inputs: right = number of squares to move to the right
#@Inputs: down = number of squares to move down
def day_3_puzzle_1(right, down):
    with open("d3_p1.txt", "r+") as f:
        line_data = [line.strip() for line in f]

    #search config 
    #search direction = right 3, down 1
    search_position = (0,0)
    number_of_trees = 0
    number_of_rows = len(line_data)
    number_of_columns = len(line_data[0])

    while search_position[1] < number_of_rows-1:
        search_position = (search_position[0] + right, search_position[1] + down)
        line = line_data[search_position[1]]
        try:
            position = line[search_position[0]]
        except IndexError: #if you reach the end before the bottom
            #reset the horizontal index
            search_position = (search_position[0] - number_of_columns, search_position[1])
            line = line_data[search_position[1]]
            position = line[search_position[0]]

        if position == "#":
            number_of_trees += 1

    return number_of_trees

def day_3_puzzle_2():

    right_shifts = [1,3,5,7,1] 
    down_shifts = [1,1,1,1,2]
    number_of_trees = list()

    for right, down in zip(right_shifts, down_shifts):
        number_of_trees.append(day_3_puzzle_1(right, down))

    product = np.prod(number_of_trees)
    return product

def main():
    print("P1 Output: ", day_3_puzzle_1(3, 1))
    print("P2 Output: ", day_3_puzzle_2())


main()
