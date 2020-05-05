import matplotlib.pyplot as plt
import math

xs = [0.01*n for n in range(-5000, 5000, 1)]

sinc = []
for x in xs:
    if x != 0:
        sinc.append(math.sin(x) / x)
    else:
        sinc.append(1)

plt.plot(xs, sinc)
plt.savefig("03 ADC and DAC/sinc.png")