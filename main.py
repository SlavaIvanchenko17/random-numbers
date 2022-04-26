import random
import time as t
import matplotlib.pyplot as plt
import numpy as np
number_in_interval = 50

def gen_number(N, l):
    y = np.zeros(N)
    x = np.zeros(N)

    for t in range(N):
        e = random.uniform(0, 1)
        y[t] = -1 / l * np.log(e)
        x[t] = t
    return [x, y]

def set_interval(data):
    current_index = 0
    count_of_intervals = 0
    current_interval = np.zeros(number_in_interval)
    data_by_intervals = np.zeros(int(len(data)/number_in_interval))
    x = np.zeros(int(len(data)/number_in_interval))


    for t in range(len(data)):
        current_interval[current_index] = data[t]

        if current_index == number_in_interval - 1:
            current_index = 0
            M = np.mean(current_interval)
            data_by_intervals[count_of_intervals] = np.mean(current_interval)
            x[count_of_intervals] = count_of_intervals*number_in_interval
            current_interval = np.zeros(number_in_interval)
            count_of_intervals += 1
        else:
            current_index += 1

    return [x, data_by_intervals]


def get_x2(data):
    M = np.mean(data)
    x2 = 0

    for t in range(len(data)):
        x2 += ((data[t] - M)**2) / M

    return np.sqrt(x2)

def math_expectation(data):
    return np.mean(data)

def dispersion(data):
    return np.var(data)


N = int(input("Number of points = "))
Lambda = float(input("Lambda = "))
signal = gen_number(N, Lambda)
data_by_intervals = set_interval(signal[1])
plt.figure(1)
plt.bar(data_by_intervals[0], data_by_intervals[1], width=number_in_interval)
plt.title('Random numbers by interval')
plt.show()
print("X2 = " + str(get_x2(data_by_intervals[1])))
print("Mathematical expectation = " + str(math_expectation(data_by_intervals[1])))
print("Dispersion = " + str(dispersion(data_by_intervals[1])))
