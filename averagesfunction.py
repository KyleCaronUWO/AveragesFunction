import math

ls = [2, 7, 20, 15, 90, 28]

def calculate_average(ls):
    add = sum(ls)
    length = len(ls)
    div = add / length
    return div

print(calculate_average(ls))