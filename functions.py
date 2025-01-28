# Double the value of a number.
# Input: a number to be doubled
# Result: a number
def double(n:int) -> int:
    result = n * 2
    return result

# Based on the value of the parameter, the result of the function should be 6.
# The issue is that the statement was multiplying the number by itself rather than by 2.

#Question: If test_double_one had been the only testing function, the tests would have passed the first time.
# Would that have meant that the code was correct? While waiting to demonstrate completion of the lab, ponder how many tests one might
# need to sufficiently test this function.

# Q answer) The code would not have been correct if it passed test_double_one as it tested a special case where the square = double
# I would only need one test to sufficiently test this function as there would only be 3 special cases to avoid; I would just have to
# choose to test cases where the double will surely not equal the square of the function or any other operations on the function.