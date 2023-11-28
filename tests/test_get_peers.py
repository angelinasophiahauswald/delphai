from src.text_similarity.company_similarity import get_peers

def test_get_peers():
    url = 'theyield.com'
    expected_result = [('pycno.co', 0.12099741662881197), ('kitro.ch', 0.11628033683848055), ('cogz.co', 0.11507157133858137), ('avanijal.com', 0.11070501769331521), ('panacea.ag', 0.10395311653314114), ('grownetics.co', 0.09880711790430399), ('yara.com', 0.09454386380263771), ('fazlagida.com', 0.09276676774420303), ('kakaxi.me', 0.09052731764826766), ('onefarm.io', 0.08810912244012901)]
    peers = get_peers(url, "data/company_collection.json")
    assert peers == expected_result