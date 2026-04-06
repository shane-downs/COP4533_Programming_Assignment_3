import time
import sys
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


def run(input_path, output_path):
    char_values, A, B = read_input(input_path)
    #start = time.perf_counter()
    res, grid = max_subsequence_value(char_values, A, B, debug=True)
    #end = time.perf_counter()
    solution = get_solution(grid, A, B, char_values)

    print(f"Input:  {input_path}")
    print(f"Result (HVLCS): {res}")
    print(f"Subsequence: {solution}")
    print()

    with open(output_path, "w") as output_file:
        output_file.write(str(res))
        output_file.write("\n")
        output_file.write(solution)


if __name__ == "__main__":
    if len(sys.argv) > 1:
        # Run on a specific input file
        # how to run -> python main.py ../input/example.in
        input_path = sys.argv[1]
        # make output path: ../input/foo.in -> ../output/foo.out
        filename = input_path.split("/")[-1].replace(".in", ".out")
        output_path = f"../output/{filename}"
        run(input_path, output_path)
    else:
        # Run all 10 test cases
        for i in range(1, 11):
            print(f"--- test case {i} ---")
            run(f"../input/input_{i}.in", f"../output/output_{i}.out")

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
#     Code to print time-elapsed
#     # print(end-start)
#     with open(f"../output/{file_name}.out", "w") as output_file:
#         output_file.write(str(res))
#         output_file.write("\n")
#         output_file.write(get_solution(grid, A, B))
