"""
https://ethanweed.github.io/pythonbook/landingpage.html
https://github.com/weijie-chen/Basic-Statistics-With-Python
https://realpython.com/python-statistics/
"""

import statistics as stats
from statistics import mean, median, mode, stdev

numbers = [44,66,33,67,232,12,45,67,89,90,100,101,102,103,104,105]
print(sum(numbers))  # Sum of all numbers
print(stats.mean(numbers))  # Mean of the numbers
print(stats.median(numbers))  # Median of the numbers
print(stats.mode(numbers))  # Mode of the numbers
print(stats.stdev(numbers))  # Standard deviation of the numbers
print(stats.variance(numbers))  # Variance of the numbers
print(stats.pstdev(numbers))  # Population standard deviation


rollings = np.random.randint(1, 7, 1000)

fig, ax = plt.subplots(figsize=(9, 9))
n, bins, patches = ax.hist(rollings, bins=6)
ax.set_title("Frequency Histogram of 1000 Times of Rolling a Dice", size=19)
ax.set_xlim(0, 7)
ax.set_ylim(0, 400)
plt.show()