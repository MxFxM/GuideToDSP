# histo is a list where the index is the value of the bin
# and the value in the list is the number of samples
# of the bin value
# N is number of all samples
def histogram_mean(histo, N):
    sum = 0
    for value, samples in enumerate(histo):
        sum = sum + value * samples
    mean = sum / N
    return mean

def histogram_variance(histo, N):
    sum = 0
    mean = histogram_mean(histo, N)
    for value, sample in enumerate(histo):
        sum = sum + (value - mean)**2 * samples
    variance = sum / (N - 1)

# when replacing the division by bin_size with a multiplication
# it already gets faster
def create_histo(list_of_samples, number_of_bins, min, max):
    histo = [0 for _ in range(number_of_bins)]
    bin_size = (max - min) / number_of_bins
    for sample in list_of_samples:
        histo[round(sample / bin_size)] = \
            histo[round(sample / bin_size)] + 1

