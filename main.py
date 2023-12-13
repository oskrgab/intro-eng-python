import numpy as np
import matplotlib.pyplot as plt

# Define a function
def my_func(x_arr):
  # Initialize list to store results
  result = []
  # We will assume that 'x_arr' is always an array or iterable
  for x in x_arr:
    if x > 0:
        result.append(2*x + 5)
    else:
        result.append(x**2 - 3)

  return result

# Create 100 values of x between -5 and 5
my_x_arr = np.linspace(-5,5,100)
# Evaluate equation at x
y = my_func(my_x_arr)

# Plot x and y
fig, ax = plt.subplots(figsize=(4, 2))
ax.plot(my_x_arr, y)
plt.show()
