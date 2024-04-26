from scipy.spatial import distance
import numpy as np


"""
    Calculate the Euclidean distance for any sample in the  Dataset.

    Args:
        Dataset

    Returns:
        a Matrix which include The Euclidean distance between the samples .
"""



def edge_creator(dataset , threshold):



    size = len(dataset)
    adjacency_matrix = np.zeros((size, size))



    #calculate distance
    for i in range(size):
        for j in range(i+1, size):
            euclidean_distance = distance.euclidean(dataset.iloc[i].values, dataset.iloc[j].values)
            adjacency_matrix[i][j] = euclidean_distance
            adjacency_matrix[j][i] = euclidean_distance


    #normalize the distance between 0 to 1
    min_dist = np.min(adjacency_matrix)
    max_dist = np.max(adjacency_matrix)
    normalized_matrix = (adjacency_matrix - min_dist) / (max_dist - min_dist)


    normalized_matrix = (normalized_matrix <= threshold) * normalized_matrix

    return normalized_matrix




