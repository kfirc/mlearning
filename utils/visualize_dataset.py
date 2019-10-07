import math
import matplotlib.pyplot as plt

from config import Config

FIGURE_CONFIG = dict(
    figsize=(6, 6),
)

DEFAULT_SUBPLOT_CONFIG = dict(
    left=0,
    right=1,
    bottom=0,
    top=1,
    hspace=0.05,
    wspace=0.05
)


def add_image_to_subplot(axis, image, target):
    # Display an image at the i-th position
    axis.imshow(image, cmap=plt.cm.gray_r, interpolation='sinc')
    # label the image with the target value
    axis.text(0, 7, str(target))


def visualize_dataset(dataset):
    # Find the dataset square shape
    square_shape = [math.ceil(dataset.data.shape[1] ** 0.5)] * 2
    size = dataset.data.shape[1]

    figure = configure_pyplot_figure()

    # For each of the 64 images
    for i in range(size):
        image = dataset.images[i]
        target = dataset.target[i]

        # Initialize the subplots: add a subplot in the grid of 8 by 8, at the i+1-th position
        ax = figure.add_subplot(*square_shape, i + 1, xticks=[], yticks=[])
        add_image_to_subplot(ax, image, target)

    # Show the plot
    if Config.DISPLAY_PLOT:
        plt.show()


def configure_pyplot_figure(**subplot_config):
    figure_configuration = dict(FIGURE_CONFIG)
    subplots_configuration = dict(DEFAULT_SUBPLOT_CONFIG)
    subplots_configuration.update(subplot_config)

    # Figure size (width, height) in inches
    figure = plt.figure(**figure_configuration)

    # Adjust the subplots
    figure.subplots_adjust()
    return figure
