import matplotlib.pyplot as plt
import numpy as np
import random

if __name__ == '__main__':
    for _ in range(200):
        x0 = random.uniform(-1, 1)
        kSet = np.arange(0.0, 2.0, 0.01)
        xSet = []
        for k in kSet:
            x = x0
            for _ in range(500):
                x = 1 - k * x ** 2
            xSet.append(x)
        plt.scatter(kSet, xSet, c = 'black', marker = '.')
    plt.xlabel('k')
    plt.ylabel('x')
    plt.title('x_{k+1} = 1 - x_{k}^2')
    plt.show()