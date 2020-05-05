def random_gauss(mean, standard_deviation):
    sum = 0
    for _ in range(12):
        sum = sum + random()
    centered_around_zero = sum - 6
    deviated = centered_around_zero * standard_deviation
    gauss_value = deviated + mean
    return gauss_value

# use the returned value as the next seed
# and use any number (for example time) as the starting seed
# pick a, b and c appropriately
def random(seed, a, b, c):
    rand = (a*seed + b) % c
    return rand
