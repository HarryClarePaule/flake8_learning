import numpy as np


def calculate_mean(arr):
    """
    Calculates the mean of an array using NumPy.

    Args:
        arr (numpy.ndarray): The input array.

    Returns:
        float: The mean of the array.
    """
    return np.mean(arr)


my_array = np.array([1, 2, 3, 4, 5, 7])
mean_value = calculate_mean(my_array)
print(mean_value)


class RunningMeanCalculator:
    def __init__(self):
        self.count = 0
        self.mean = 0.0

    def update(self, new_data):
        self.count += 1
        self.mean = self.mean + (new_data - self.mean) / self.count

    def get_mean(self):
        return self.mean


mean_calculator = RunningMeanCalculator()
data = [1, 2, 3, 4, 5]
for point in data:
    mean_calculator.update(point)
    current_mean = mean_calculator.get_mean()
    print(f"Running mean: {current_mean}")
