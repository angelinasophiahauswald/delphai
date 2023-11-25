import json

def read_json():
    file = open('data/company_collection.json')
    data = json.load(file)
    file.close()

if __name__ == "__main__":
    read_json()