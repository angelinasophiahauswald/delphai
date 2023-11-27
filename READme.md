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
- input: path to the data file
- output: returns a list of dictionaries, each element containing the information of one company from the json input file 

### read_description
- input: list of dictionaries, each element containing the information of one company from the json input file and the url of the company of which the description should be returned
- output: returns the description of the input company

### preprocess_description
- input: description text of a company
- output: tokenized, lemmatized, stemmed description without punctuation

### text_similarity
- input: input company description and the company description that the input company description should be compared to
- output: returns the similarity measure between both 

### get_peers
- input: input url handed over through the command line
- output: returns a list of the ten best candidates in a descending order

### write_output
- input: list of tuples of the ten best candidates
- output: creates an output-directory and a txt-file, each txt-file (filename is the input url) contains the ten best candidates for the input url