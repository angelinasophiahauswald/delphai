# ML Working Student | Assessment task



## Setting Up Virtual Enviroment

- Install a Virtualenv
 `pip install virtualenv`
- Create python virtual enviroment
 `python -m venv .venv`
- Activate virtual enviroment
 `source .venv/bin/activate`
- Install requirements from requirements.txt
 `pip install -r requirements.txt`

## Running tests
- Run all tests
 `pytest`

## Function description
### read_json
- Input: path to the data file
- Output: returns a list of dictionaries, each element containing the information of one company from the json input file 

### read_description
- Input: list of dictionaries, each element containing the information of one company from the json input file and the url of the company of which the description should be returned
- Output: returns the description of the input company

### preprocess_description
- Input: description text of a company
- Output: tokenized, lemmatized, stemmed description without punctuation

### text_similarity
- Input: input company description and the company description that the input company description should be compared to
- Output: returns the similarity measure between both 

### get_peers
- Input: input url handed over through the command line
- Output: returns a list of the ten best candidates in a descending order

### write_output
- Input: list of tuples of the ten best candidates
- Output: creates an output-directory and a txt-file, each txt-file (filename is the input url) contains the ten best candidates for the input url