def gaussian_probability(x, mean, standard_deviation):
    factor = 1 / (math.sqrt(2 * math.pi) * standard_deviation)
    exponent = -((x - mean)**2 / (2 * standard_deviation**2))
    probability = factor * math.e**(factor)
    return probability
