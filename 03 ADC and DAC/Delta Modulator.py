import math
import matplotlib.pyplot as plt

time = [n for n in range(400)]

inputsignal = [math.sin(n*0.01) for n in time]
outputsignal = []
reconstructedsignal = []

capacitorvoltage = 0
for t in time:
    if inputsignal[t] > capacitorvoltage:
        outputsignal.append(1)
        capacitorvoltage = capacitorvoltage + 0.01
    else:
        outputsignal.append(0)
        capacitorvoltage = capacitorvoltage - 0.01
    reconstructedsignal.append(capacitorvoltage)

plt.plot(time, inputsignal)
plt.plot(time, outputsignal)
plt.plot(time, reconstructedsignal)

plt.savefig("03 ADC and DAC/deltamodulator.png")