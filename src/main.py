from dp import *

def read_input(filename):
    with open(filename, "r") as f:
        lines = f.read().splitlines()
        K = int(lines[0])
        char_values = dict()
        for i in range(1, K + 1):
            char, value = lines[i].split(" ")
            char_values[char] = int(value)

        A = str(lines[K + 1])
        B = str(lines[K + 2])

    return char_values, A, B
    
    
if __name__ == "__main__":
    for i in range(1,11):
        char_values, A, B = read_input(f"../input/input_{i}.in")
        res, grid = max_subsequence_value(char_values, A, B, debug=True)
        print_dp(grid, A, B)
        print()
        print(res)
        print(get_solution(grid, A, B))
        with open(f"../output/output_{i}.out", "w") as output_file:
            output_file.write(str(res))
            output_file.write("\n")
            output_file.write(get_solution(grid, A, B))
    