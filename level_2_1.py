#!/usr/bin/env python3
"""
    Level 2.1
    
    Examples of input vs output:
    solution(["1.11", "2.0.0", "1.2", "2", "0.1", "1.2.1", "1.1.1", "2.0"])
        ['0.1', '1.1.1', '1.2', '1.2.1', '1.11', '2', '2.0', '2.0.0']
    solution(["1.1.2", "1.0", "1.3.3", "1.0.12", "1.0.2"])
        ['1.0', '1.0.2', '1.0.12', '1.1.2', '1.3.3']
    solution({"1.11", "2.0.0", "1.2", "2", "0.1", "1.2.1", "1.1.1", "2.0"})
        ['1.0', '1.0.2', '1.0.12', '1.1.2', '1.3.3']
    solution({"1.1.2", "1.0", "1.3.3", "1.0.12", "1.0.2"})
        ['1.0', '1.0.2', '1.0.12', '1.1.2', '1.3.3']
"""

def version_gt(x, y):
    version_x = [int(num) for num in x.split('.')]
    version_y = [int(num) for num in y.split('.')]

    for i in range(max(len(version_x), len(version_y))):
        num_x = version_x[i] if len(version_x) > i else -1
        num_y = version_y[i] if len(version_y) > i else -1
        if num_x == num_y:
            continue
        return num_x > num_y
    return False

def solution(versions):

    new_list = []
    for version in versions:
        index = 0
        for target in new_list:
            if not version_gt(version, target):
                break
            index += 1
        new_list.insert(index, version)
    return new_list
