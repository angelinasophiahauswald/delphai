# ML Working Student | Assessment task



## Setting Up Virtual Enviroment

- Install a Virtualenv
 `pip3 install virtualenv`
- Create python virtual enviroment
 `python -m venv .venv`
- Activate virtual enviroment
 `source .venv/bin/activate`
- Install requirements from requirements.txt
 `pip3 install -r requirements.txt`

## Running tests
- Run all tests
 `pytest`

## Function description
### read_json
- Input: path to the data file
- Output: returns a list of dictionaries, each element containing the information of one company from the json input file 

### read_description
- Input: list of dictionaries, each element containing the information of one company from the json input file and the URL of the company of which the description should be returned
- Output: returns the description of the input company

### preprocess_description
- Input: description text of a company
- Output: tokenized, lemmatized, stemmed description without stop words and punctuation

### text_similarity
- Input: input company description and the company description that the input company description should be compared to
- Output: returns the cosine similarity between both 

### get_peers
- Input: input URL handed over through the command line
- Output: returns a list of the top ten similar companies sorted by similarity in descending order

### write_output
- Input: list of tuples of the ten best candidates
- Output: creates an output-directory and a txt-file, each txt-file (filename is the input URL) contains the ten best candidates for the input URL along with their similarity scores

## What does this program do?
- The script starts by reading a JSON file containing information about different companies. Each company has a URL and a description.
- The script expects two command-line arguments:
    - <path_to_data_file>: The path to the JSON file containing company data.
    - <input_company_url>: The URL of the company for which similar companies need to be found.

- Each company description undergoes a series of preprocessing steps to standardize the text:
    - Lowercasing: Convert all characters in the description to lowercase.
    - Removing Punctuation: Eliminate punctuation and special characters.
    - Tokenization: Break the description into individual words (tokens).
    - Removing Stopwords: Exclude common English stopwords (e.g., "the," "and," "is").
    - Lemmatization: Reduce words to their base or root form.

- The preprocessed descriptions are then transformed into TF-IDF vectors using the TfidfVectorizer. TF-IDF is a numerical statistic that reflects the importance of a word in a document relative to a collection of documents (corpus). It helps to capture the significance of words in the context of a specific document.

- Cosine similarity is computed between the TF-IDF vectors of the input company and each other company in the dataset. Cosine similarity is a metric that measures the cosine of the angle between two vectors. It ranges from -1 (completely dissimilar) to 1 (completely similar), with 0 indicating orthogonality.

- The script identifies the ten companies with the highest cosine similarity scores to the input company, which means these companies are considered the most similar to the input company based on their TF-IDF representations.

## What are its weaknesses?
- The script relies solely on the TF-IDF representation of text, which may not fully capture the semantic meaning or context of the company descriptions.

- It tokenizes and preprocesses text without considering the sequential order of words. This can lead to a loss of important information, especially in cases where word order matters for understanding the meaning of the text.

- The effectiveness of the approach heavily depends on the preprocessing choices made, such as lemmatization, stemming, and stopword removal. Different choices might yield different similarity scores and rankings.

- The script does not handle typos or synonyms, which might lead to mismatches in the similarity calculation. 

## Future improvements
- It would be helpful to integrate word embeddings to capture semantic relationships between words.

- Instead of representing documents as bags of words, it could be considered using methods like Doc2Vec or other paragraph embedding techniques. These methods can also capture the semantic meaning of entire documents and handle word order.

- Additionally, methods to address synonyms and polysemy can be used, such as expanding the vocabulary with synonyms or utilizing word sense disambiguation techniques.

- Another option would be to implement dynamic term weighting schemes that adjust weights based on the importance of terms in specific contexts.
