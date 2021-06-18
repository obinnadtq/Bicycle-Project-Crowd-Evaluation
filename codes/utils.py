# get the data from the json file
def read_data_from_json(data, number):
    return data['results']['root_node']['results'][number]['results']
