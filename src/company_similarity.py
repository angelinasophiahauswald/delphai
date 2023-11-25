import sys
import json

def read_json(input_file):
    # TODO: check if file exists
    file = open(input_file)
    data = json.load(file)
    file.close()
    return data

if __name__ == "__main__":
    if len(sys.argv) < 2:
        # TODO: pretty error messages
        print("Missing path to data file")
    else:
        input_file = sys.argv[1]
        print(read_json(input_file))