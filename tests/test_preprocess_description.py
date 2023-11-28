from src.text_similarity.company_similarity import preprocess_description

def test_preprocess_description():
    input_text = "We want to make possible an agriculture that inspires.  This means food production that is profitable for farmers, safe for consumers and good for the environment.We need to produce 70 percent more food by 2050 to feed the world with less fuel, land, fertiliser and water. We have to do this at the same time as dealing with unprecedented impacts..."
    expected_preprocessed_text = "want make possible agriculture inspires mean food production profitable farmer safe consumer good environmentwe need produce 70 percent food 2050 feed world le fuel land fertiliser water time dealing unprecedented impact"
    result = preprocess_description(input_text)
    assert result == expected_preprocessed_text
