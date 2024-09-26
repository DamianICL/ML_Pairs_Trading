import numpy as np

def log_transform(data):
    data[:] = np.log(data)

