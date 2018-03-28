
def prepare_data_to_work(filepath):
    with open(filepath, 'r') as file:
        readed_lines = [line.split(';') for line in [line.replace(',', '.') for line in file.readlines()]]

    return readed_lines



