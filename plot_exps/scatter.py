import numpy as np
import matplotlib.pyplot as plt
from colour import Color


def create_input(nr_bivariate):
    return [create_bivariate_sample() for i in range(nr_bivariate)]

def create_bivariate_sample():
    return (create_sample(),create_sample())

def create_sample():
    offset = np.random.uniform(low=3, high=7)
    width = np.random.uniform(high=2)
    return np.array([offset + np.random.normal(offset, width) for i in range(200)])

def main():
    data = create_input(5)
    red = Color("red")
    blue = Color("blue")
    colors = [x.rgb for x in list(red.range_to(blue, len(data)))]
    fig, ax = plt.subplots()
    for i in range(len(data)):
        plt.scatter(
            data[i][0],
            data[i][1],
            color=colors[i])
    plt.show()
    
if __name__ == '__main__':
    main()