def max_subsequence_value(char_values, A, B, debug=False):
    dp = [[0] * (len(B) + 1) for _ in range(len(A) + 1)]  # Build the 2D DP array with extra row/col for base case
    # i.e. you can't have a subsequence with an empty string, that max value is always 0
    
    for i in range(len(A) - 1, -1, -1):
        for j in range(len(B) - 1, -1, -1):
            if A[i] == B[j]:  # Chars match
                dp[i][j] = dp[i + 1][j + 1] + char_values[A[i]]
            else:  # Chars dont match
                dp[i][j] = max(dp[i + 1][j], dp[i][j + 1], dp[i + 1][j + 1])

    if debug:  # DEBUG PARAM FOR PRINTING THE FILLED/COMPUTED GRID, USED WITH print_dp()
        return dp[0][0], dp
    else:
        return dp[0][0]
    
def get_solution(dp, A, B): # Post-processing/backtracking to get solution subsequence
    i = 0
    j = 0
    res = ""
    while i < len(A) and j < len(B):
        # Chars match, collect and move diagonally (no need to check either substring)
        if A[i] == B[j]:
            res += A[i]
            i += 1
            j += 1
        # Chars don't match, move toward max substring value of A or B depending on max
        else:
            if dp[i + 1][j] > dp[i][j + 1]:  # Don't care about equal, spec says just output any 1 of the solutions
                i += 1
            else:
                j += 1
    return res
                

def print_dp(dp, A="", B=""):  # DEBUG HELPER
    if B:
        print("    ", "  ".join(f"{c:>3}" for c in B))
    for i, row in enumerate(dp):
        label = A[i-1] if A and i > 0 else " "
        print(f"{label} |", " | ".join(f"{v:>3}" for v in row), "|")