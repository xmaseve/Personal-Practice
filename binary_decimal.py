'''
Convert binary number to decimal number
'''
def binary_decimal(binary_digit):
  n = len(str(binary_digit)) - 1
  total = 0
  for i in str(binary_digit):
    total += 2**n * int(i)
    n -= 1
  return total
