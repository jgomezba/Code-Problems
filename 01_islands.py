test_matrix = [
    [1, 0, 0, 0],
    [0, 0, 1, 0],
    [0, 1, 1, 1],
    [0, 1, 0, 0],
    [0, 0, 1, 0],
    [0, 1, 0, 0]
]

def get_one_positions(matrix):
    one_list = []
    rows, columns = len(matrix), len(matrix[0])
    for row in range(rows):
        for column in range(columns):
            if matrix[row][column] == 1:
                one_list.append((row,column))
    return one_list

def get_islands(one_positions_list, visited, row, column):
    island = []
    stack = [(row, column)]
    while stack:
        row, column = stack.pop()
        island.append((row,column))
        move_up = (row-1, column)
        move_down = (row+1, column)
        move_left = (row, column-1)
        move_right = (row, column+1)
        
        if move_up in one_positions_list and move_up not in visited:
            stack.append(move_up)
            visited.append(move_up)
        if move_down in one_positions_list and move_down not in visited:
            stack.append(move_down)
            visited.append(move_down)
        if move_left in one_positions_list and move_left not in visited:
            stack.append(move_left)
            visited.append(move_left)
        if move_right in one_positions_list and move_right not in visited:
            stack.append(move_right)
            visited.append(move_right)
    return [island, visited]

if __name__ == "__main__":
    islands = []
    visited_list = []
    one_positions = get_one_positions(test_matrix)
    for tuple in one_positions:
        if tuple not in visited_list:
            row, col = tuple
            result = get_islands(one_positions, visited_list, row, col)
            islands.append(result[0])
            visited_list.extend(result[1])

    for i in range(len(islands)):
        print(f"Found island {i+1} : {islands[i]}")
