import random

def get_rand_matrix(max_size=5):
    rows = random.randint(2, max_size)
    cols = random.randint(2, max_size)
    matrix = [[random.randint(1,100) for _ in range(cols)] for _ in range(rows)]
    
    return matrix, rows, cols

def get_all_paths(n, m, path = "", paths = []):
    if n == 0 and m == 0:
        paths.append(path)
        return paths
        
    if n > 0:
        # Move down
        get_all_paths(n-1, m, path + "D", paths)
    if m > 0:
        # Move rigth
        get_all_paths(n, m-1, path + "R", paths)
    
    return paths

def get_gains(paths, matrix):
    gain_list = []
    for path in paths:
        init_row = 0
        init_col = 0
        gain = 0
        for movement in path:
            if movement == "D":
                init_row = init_row + 1
                gain += matrix[init_row][init_col]
            else:
                init_col = init_col + 1
                gain += matrix[init_row][init_col]
        gain_list.append(gain)
    return gain_list

if __name__ == "__main__":
    print()
    matrix, rows, cols = get_rand_matrix()
    print(f"Matrix with dimension {rows}x{cols}")
    for row in matrix:
        print(row)
    print()
        
    paths = get_all_paths(rows-1, cols-1)
    gains_list = get_gains(paths, matrix)
    
    for i in range(len(paths)):
        print(f"Path found: {paths[i]} with value: {gains_list[i]}")
        
    print()
    best_index = gains_list.index(max(gains_list))
    print(f"Best path found {paths[best_index]} with value: {gains_list[best_index]}")