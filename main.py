from tfidf import get_tfidf_matrix
from text_utils import read_file
from similarity import cosine_similarity

text_files = ['test1.txt','test2.txt']
docs = [read_file(file_name) for file_name in text_files]
tfidf_matrix = get_tfidf_matrix(docs)

vector1 = tfidf_matrix.getrow(0).toarray()[0]
vector2 = tfidf_matrix.getrow(1).toarray()[0]
similarity = cosine_similarity(vector1,vector2)

print("Similarity between %s and %s is -> %f" % (text_files[0],text_files[1],similarity*1))
#if its over 0.4 then its likely to be similar