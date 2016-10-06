import numpy as np
import matplotlib.pyplot as plt
from colour import Color


SAMPLE_CARDINALITY = 10000
NR_DISTRIBUTIONS = 3


def create_input(nr_bivariate):
    return [shift(random_rotate(create_bivariate_sample())) for i in range(nr_bivariate)]


def create_bivariate_sample():
    return np.array([create_sample(), create_sample()])


def random_rotate(array):
    theta = np.random.uniform(low=0, high=(2 * np.pi))
    rot_matrix = np.array([[np.cos(theta), -np.sin(theta)],
                          [np.sin(theta),  np.cos(theta)]])
    return np.dot(rot_matrix, array)


def shift(bivariate):
    offset_x = np.random.uniform(low=0, high=5)
    offset_y = np.random.uniform(low=0, high=5)
    for i in range(SAMPLE_CARDINALITY):
        bivariate[0][i] += offset_x
        bivariate[1][i] += offset_y
    return bivariate


def create_sample():
    width = np.random.uniform(low=0, high=2)
    return np.array([np.random.normal(0, width) for i in range(SAMPLE_CARDINALITY)])


def main():
    data = create_input(NR_DISTRIBUTIONS)
    red = Color("red")
    blue = Color("blue")
    colors = [x.rgb for x in list(red.range_to(blue, len(data)))]
    plt.subplots()
    for i in range(len(data)):
        plt.scatter(
            data[i][0],
            data[i][1],
            color=colors[i],
            s=1
        )

    plt.xlabel("X")
    plt.ylabel("Y")
    plt.title("{0} bivariate distribution{1}".format(NR_DISTRIBUTIONS, "" if NR_DISTRIBUTIONS == 1 else "s"))

    plt.show()
    
if __name__ == '__main__':
    main()
