# get the data from the json file
def read_data_from_json(data, number):
    return data['results']['root_node']['results'][number]['results']

def get_property(data, arr, prop):
    for i in range(0, len(data)):
        arr.append(data[i][prop])
        
        


def get_list_of_dataframes(annotators, dataframe, reference_data_answers):
    dataframes = []
    for i in range(0, len(annotators)):
        new_col = []
        new_dataframe = dataframe[dataframe['Annotators'] == annotators[i]]
        for j in range(0, len(new_dataframe['Images'])):
            new_col.append(reference_data_answers[new_dataframe['Images'].iloc[j][:-4]])
        new_dataframe['Reference'] = new_col
        dataframes.append(new_dataframe)
    return dataframes