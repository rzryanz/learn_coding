import math

# Computes the logarithm base 10 of the signal-to-noise ratio
ratio = signal_power / noise_power
decibles = 10 * math.log10(ratio)
print(decibles)

# Finds the sine of given radians
radians = 0.7
height = math.sin(radians)
print(height)

# To convert from degrees to radians, divide by 360 and multiply by 2π
degrees = 45
radians = degrees / 360.0 * 2 * math.pi
print(math.sin(radians))
