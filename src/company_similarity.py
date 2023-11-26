import sys
import json
import transformers

def read_json(input_file):
    # TODO: check if file exists
    file = open(input_file)
    data = json.load(file)
    file.close()
    return data

def test(companies, url):
    for company in companies:
        if company['url'] == url:
            return company['description']

def text_similarity(text1, text2):
    # Load the BERT model
    model = transformers.BertModel.from_pretrained('bert-base-uncased')

    # Tokenize and encode the texts
    text1 = "This is the first text."
    text2 = "This is the second text."
    encoding1 = model.encode(text1, max_length=512)
    encoding2 = model.encode(text2, max_length=512)

    # Calculate the cosine similarity between the embeddings
    similarity = numpy.dot(encoding1, encoding2) / (numpy.linalg.norm(encoding1) * numpy.linalg.norm(encoding2))
    print(similarity)


if __name__ == "__main__":
    if len(sys.argv) < 3:
        # TODO: pretty error messages
        print("Missing path to data file")
    else:
        input_file = sys.argv[2]
        data = read_json(input_file)
        input_company = sys.argv[1]
        test(data, input_company)