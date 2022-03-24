# Assume that we execute the following assignment statements:
# width = 17
# height = 12.0
#
# For each of the following expressions, write the value of the expression and the type.
# 1) width//2
# 2) width/2.0
# 3) height/3
# 4) 1 + 2 * 5

width = 17
height = 12.0

py2_division_width= width // 2
# value = 8
# type is integer
print(py2_division_width)
print(type(py2_division_width))

py3_division_width = width / 2.0
# value = 8.5
# type is float
print(py3_division_width)
print(type(py3_division_width))

py3_division_height = height / 3
# value = 4.0
# type is float
print(py3_division_height)
print(type(py3_division_width))

x = 1 + 2 * 5
# value = 11
# type is integer
print(x)
print(type(x))
