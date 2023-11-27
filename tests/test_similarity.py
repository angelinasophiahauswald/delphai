from src.text_similarity.company_similarity import text_similarity

def test_similarity():
    text_1 = "Daikin Industries, Ltd. is a global leader in the market of commercial and industrial use air conditioning systems, with more than 40% of the market share in Japan and a well-established presence in China,"
    text_2 = "Gradient Technology provides chemical engineering solutions. Its chemical engineering services include research and development, project management, laboratory, pilot plant, plant engineering, and process automation."
    similarity = text_similarity(text_1, text_2)
