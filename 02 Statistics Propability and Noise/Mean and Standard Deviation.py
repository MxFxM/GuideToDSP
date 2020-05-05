def mean(list):
    sum = 0
    for value in samples:
        sum = sum + value
    mean = sum / N
    return mean

def average_deviation(list):
    mean = mean(list)
    sum = 0
    for value in samples:
        deviation = abs(value - mean)
        sum = sum + deviation
    average_deviation = sum / N
    return average_deviation

def standard_deviation(list):
    mean = mean(list)
    sum = 0
    for value in samples:
        deviation = (value - mean)**2
        sum = sum + deviation
    squared_deviation = sum / (N-1)
    average_deviation = sqrt(squared_deviation)
    return average_deviation

class running_statistics:
    def __init__(self):
        self.N = 0
        self.sum = 0
        self.sq_sum = 0
    def new_sample(self, value):
        self.N = self.N + 1
        self.sum = self.sum + value
        self.sq_sum = self.sq_sum + value**2
    def get_mean(self):
        if (self.N <= 0):
            return 0
        mean = self.sum / self.N
        return mean
    def get_standard_deviation(self):
        if (self.N <= 1):
            return 0
        variance = (self.sq_sum-(self.sum**2 / self.N))/(self.N-1)
        standard_deviation = sqrt(variance)
        return standard_deviation

def snr(mean, standard_deviation):
    snr = mean / standard_deviation
    return snr

def cv(mean, standard deviation):
    cv = (standard_deviation / mean) * 100
    return cv
