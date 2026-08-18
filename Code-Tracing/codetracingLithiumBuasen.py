# =============================================================================================================================================
# Code #1: Safe character printing

# a. If name is “Joseph The Dreamer” and nChar is 5, what will be the output of the code above and why?
# Output:
#     J
#     o
#     s
#     e
#     p
# Why: range(5) iterates through indices 0 to 4. For each index i, name[i] prints the character at that index on a new line.

# b. Using the same name and nChar is 20, what now is the output and why?
# Output:
#     IndexError: string index out of range
# Why: name contains 18 characters (indices 0 through 17). When the loop reaches i = 18, Python attempts to access an index that does not exist in the string.

## c. If there is an error message encountered in letter b, how will you be able to modify the code so that the error message will not appear.
def greet_students_v1(name, nChar):
    # Safe guard against IndexError
    limit = min(nChar, len(name))
    for i in range(limit):
        print(name[i])

# =============================================================================================================================================
# Code #2: Inverted triangle printer

# a. Find the syntax error and modify it.  Please identify the error and what did you do to fix it?
# Error: Line 2 is missing a colon : at the end of the for statement (for i in range(nChar)).
# Fix: Add a colon : at the end of line 2.

## b. The code should be able to display a given name as an inverted triangle, please fix the code in order for it to do that.  See sample output below if entered name is Joseph
def greet_students_v2(name, nChar):
    for i in range(nChar):
        print(name[0 : nChar - i])

# =============================================================================================================================================
# Code #3: Sum of squared numbers function

# a. You are tasked to create the needed function/s that will return the sum of all squared numbers from 1 to n.
def sum_of_squared(n):
    return sum(i ** 2 for i in range(1, n + 1))

# =============================================================================================================================================
# Demonstration / Test execution
if __name__ == "__main__":
    print("--- Code #1 Test ---")
    greet_students_v1("Joseph The Dreamer", 5)
    
    print("\n--- Code #2 Test ---")
    test_name = "Joseph"
    greet_students_v2(test_name, len(test_name))
    
    print("\n--- Code #3 Test ---")
    n = 0
    while n < 1 or n > 100:
        n = int(input("Enter a Number from 1 to 100 : "))
    print("Sum of all squared numbers is", sum_of_squared(n))