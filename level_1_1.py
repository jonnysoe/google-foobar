"""
    Level 1.1
    
    Examples of input vs output:
    solution([2, 12, 56, 5], [5, 56, 4, 2, 12])
        4
"""

def solution(x, y):
    nums = [num for num in x if num not in y]
    if not nums:
        nums = [num for num in y if num not in x]
    # This assumes there is always 1 extra number in a list
    # There should be a better way to solve this
    return nums[0]
