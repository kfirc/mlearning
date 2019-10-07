def shapes(dataset):
    return dict(
        # Inspect the data shape
        data=dataset.data.shape,
        # Inspect the target shape
        target=dataset.target.shape,
        # Inspect the shape
        images=dataset.images.shape,
    )


def reshape_images_to_data(dataset):
    data_shape = shapes(dataset)['data']
    return dataset.images.reshape(data_shape)
