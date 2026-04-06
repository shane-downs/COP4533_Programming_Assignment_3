import time

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
    # Code to run all the given test cases at the same time
    for i in range(1,11):
        print(f"test case {i}")
        char_values, A, B = read_input(f"../input/input_{i}.in")
        start = time.perf_counter()
        res, grid = max_subsequence_value(char_values, A, B, debug=True)
        end = time.perf_counter()
        # print_dp(grid, A, B)
        print(res)
        print(f"{get_solution(grid, A, B)} \n")
        # print(end-start)
        with open(f"../output/output_{i}.out", "w") as output_file:
            output_file.write(str(res))
            output_file.write("\n")
            output_file.write(get_solution(grid, A, B))

    # Code to run only one chosen file at a time
#     file_name = "[enter the file name]"
#     char_values, A, B = read_input(f"../input/{file_name}.in")
#     start = time.perf_counter()
#     res, grid = max_subsequence_value(char_values, A, B, debug=True)
#     end = time.perf_counter()
#     # print_dp(grid, A, B)
#     print()
#     print(res)
#     print(get_solution(grid, A, B))
#     # print(end-start)
#     with open(f"../output/{file_name}.out", "w") as output_file:
#         output_file.write(str(res))
#         output_file.write("\n")
#         output_file.write(get_solution(grid, A, B))
