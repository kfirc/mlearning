from sklearn import datasets

import numpy as np

from utils.dataset import shapes, reshape_images_to_data
from utils.visualize_dataset import visualize_dataset


def test():
    digits = datasets.load_digits()

    # Inspect the dataset shapes
    dataset_shapes = shapes(digits)
    print(f"The dataset shapes: {dataset_shapes}")

    # Inspect the unique target values
    number_digits = len(np.unique(digits.target))
    print(f"Unique target values: {number_digits}")

    # Assert that the images and the data are related by shape
    reshaped_images = reshape_images_to_data(digits)
    assert np.all(reshaped_images == digits.data)

    # Visualize the dataset
    visualize_dataset(digits)


if __name__ == "__main__":
    test()
