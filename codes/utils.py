# get the data from the json file
def read_data_from_json(data, number):
    return data['results']['root_node']['results'][number]['results']

def get_property(data, arr, prop):
    for i in range(0, len(data)):
        arr.append(data[i][prop])