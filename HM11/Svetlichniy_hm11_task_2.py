def my_add(a, b):
     result = a + b
     print(f"{a} + {b} = {result}")
     return result


from functools import reduce

numbers = [0, 1, 2, 3, 4]

reduce(my_add, numbers)