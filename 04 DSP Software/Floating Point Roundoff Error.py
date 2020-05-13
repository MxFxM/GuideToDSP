import matplotlib.pyplot as plt
import random

value = 1.0
values = []

for _ in range(5000):
    # get random values
    a = random.random() * 1000
    b = random.random() * 1000

    # add them
    value = value + a
    value = value + b

    # undo? the changes
    value = value - a
    value = value - b

    # store the result
    values.append(value)

# plot and save the results
plt.plot(values)

plt.savefig("04 DSP Software/floating point error.png")