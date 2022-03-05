import numpy as np

sr2 = np.sqrt(2)

# obstacles
obstacles = [
    np.array([
        [1.7,  1.1],
        [1.7,  2.1],
        [1.2,  2.1],
        [1.2,  1.1],
        [0.7,  0.9],
        [1.9, -0.1],
        [2.4,  0.4]]),
    np.array([
        [0.7, 1.2],
        [1.1, 1.2],
        [1.1, 2.1],
        [0.7, 2.1]]),
    np.array([
        [0.5, 1.1],
        [0.5, 2.6],
        [0.2, 2.6],
        [0.2, 1.1]]),
    np.array([
        [0.5,  1. ],
        [0.5, -0.4],
        [0.2, -0.4],
        [0.2,  1. ]]),
    np.array([
        [1.9, 1.3],
        [1.9, 2.6],
        [2.2, 2.6],
        [2.2, 1.3]]),
    np.array([
        [1.9, 1.2],
        [1.9, 1.1],
        [2.5, 1.1],
        [2.5, 1.2]]),
    ]

# vertices of the safe regions
vertices = [
    np.array([
        [ 0.2, -0.4],
        [ 0.2,  2.6],
        [-0.1,  2.6],
        [-0.1, -0.4]]),
    np.array([
        [0.2, 1. ],
        [0.5, 1. ],
        [0.5, 1.1],
        [0.2, 1.1]]),
    np.array([
        [0.7, 0.9],
        [0.7, 2.1],
        [0.5, 2.1],
        [0.5, 0.9]]),
    np.array([
        [0.7, 0.9],
        [1.2, 1.1],
        [1.2, 1.2],
        [0.7, 1.2]]),
    np.array([
        [1.1, 1.2],
        [1.2, 1.2],
        [1.2, 2.1],
        [1.1, 2.1]]),
    np.array([
        [ 0.7,  0.9],
        [ 0.5,  0.9],
        [ 0.5, -0.4],
        [ 1.9, -0.4],
        [ 1.9, -0.1]]),
    np.array([
        [1.9, 2.1],
        [1.9, 2.6],
        [0.5, 2.6],
        [0.5, 2.1]]),
    np.array([
        [ 2.5, -0.4],
        [ 2.5,  0.4],
        [ 2.4,  0.4],
        [ 1.9, -0.1],
        [ 1.9, -0.4]]),
    np.array([
        [1.7, 1.1],
        [2.4, 0.4],
        [2.5, 0.4],
        [2.5, 1.1]]),
    np.array([
        [1.7, 1.1],
        [1.9, 1.1],
        [1.9, 2.1],
        [1.7, 2.1]]),
    np.array([
        [1.9, 1.2],
        [2.2, 1.2],
        [2.2, 1.3],
        [1.9, 1.3]]),
    np.array([
        [2.5, 1.2],
        [2.5, 2.6],
        [2.2, 2.6],
        [2.2, 1.2]]),
    ]
