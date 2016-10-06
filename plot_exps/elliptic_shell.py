import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Ellipse
import scatter
from colour import Color


NR_DISTRIBUTIONS = 1


def find_angle(data):
    fit_params = np.polyfit(data[0], data[1], 1)
    print(fit_params)
    angle = np.arctan(fit_params[0])*180/np.pi
    print(angle)
    return angle


def find_center(data):
    return np.array([np.mean(data[0]), np.mean(data[1])])


def find_span(data, index):
    return max(data[index]) - min(data[index])


def get_shell(data):

    return Ellipse(
        xy=find_center(data),
        width=find_span(data, 0),
        height=find_span(data, 1),
        angle=find_angle(data)
    )


def plot_ellipse(ax, ell):
    ax.add_artist(ell)
    ell.set_clip_box(ax.bbox)
    ell.set_facecolor('red')
    ell.set_alpha(0.3)


def plot_data(data):
    plt.scatter(
        data[0],
        data[1],
        color="blue",
        s=1
    )


def main():
    bivariate_distribution = scatter.create_input(1)[0]
    fig, ax = plt.subplots()
    ell = get_shell(bivariate_distribution)

    plot_ellipse(ax, ell)
    plot_data(bivariate_distribution)

    plt.xlabel("X")
    plt.ylabel("Y")
    plt.title("{0} bivariate distribution{1} with elliptic shell".format(NR_DISTRIBUTIONS, "" if NR_DISTRIBUTIONS == 1 else "s"))
    plt.show()


if __name__ == '__main__':
    main()
