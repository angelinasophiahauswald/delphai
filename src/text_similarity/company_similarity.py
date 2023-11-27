import sys
import json
import nltk
import os
import string
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

def read_json(input_data):
    if os.path.exists(input_data) == True:
        if os.stat(input_data).st_size > 0:
            file = open(input_data)
            data = json.load(file)
            file.close()
            return data

def read_description(companies, url):
    for company in companies:
        if company['url'] == url:
            return company['description']

def preprocess_description(description):
    lowered = description.lower()
    punctuation = ''.join([char for char in lowered if char not in string.punctuation])
    tokens = word_tokenize(lowered)
    stop_words = set(stopwords.words('english'))
    tokens = [word for word in tokens if word.lower() not in stop_words]
    lemmatizer = WordNetLemmatizer()
    tokens = [lemmatizer.lemmatize(word) for word in tokens]
    preprocessed_description = ' '.join(tokens)
    return preprocessed_description

def text_similarity(input_company_description, company_description_to_compare):
    preprocessed_input = preprocess_description(input_company_description)
    preprocessed_company_description_to_compare = preprocess_description(company_description_to_compare)
    vectorizer = TfidfVectorizer()
    texts = [preprocessed_input, preprocessed_company_description_to_compare]
    tfidf_matrix = vectorizer.fit_transform(texts)
    similarity_matrix = cosine_similarity(tfidf_matrix, tfidf_matrix)
    similarity = similarity_matrix[0, 1]
    return similarity

def get_peers(company_url):
    data = read_json(input_data)
    input_company_description = read_description(data, input_url)
    result_similarities = {}
    for company in data:
        if company['url'] != company_url:
            company_description_to_compare = company['description']
            result_similarities[company['url']] = text_similarity(input_company_description, company_description_to_compare)

    sorted_similarities = sorted(result_similarities.items(), key=lambda x:x[1], reverse=True)
    return sorted_similarities[:10]

def write_output(sorted_similarities):
    path = "output"
    is_exist = os.path.exists(path)
    if is_exist == False:
        os.makedirs(path)

    file_name = "output/{}.txt".format(input_url)
    if os.path.exists(file_name) == False:
        file = open(file_name, "a")
        for candidate in sorted_similarities:
            file.write("{}: {}\n".format(candidate[0], candidate[1]))
        file.close()
    else:
        os.remove(file_name)
        file = open(file_name, "a")
        for candidate in sorted_similarities:
            file.write("{}: {}\n".format(candidate[0], candidate[1]))
        file.close()



if __name__ == "__main__":
    if len(sys.argv) < 3:
        # TODO: pretty error messages
        print("Missing path to data file")
    else:
        input_url = sys.argv[1]
        input_data = sys.argv[2]
        write_output(get_peers(input_url))
        

# TO DO:
# synopsis