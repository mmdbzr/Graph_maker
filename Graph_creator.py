import pandas as pd
from edge_creator import edge_creator






def create_graph(dataset):
    data_frame = pd.DataFrame(data=dataset.data, columns=dataset.feature_names)
    data_frame['target'] = dataset.target
    edge_weight_matrix= edge_creator(data_frame,0.3)
    print(edge_weight_matrix)
    edges_List = []


    for i in range(len(data_frame.index)):
        for j in range(i+1, len(data_frame.index)):
          if edge_weight_matrix[i][j] > 0 :
            edges_List.append((i, j,edge_weight_matrix[i][j]))




    return edges_List









