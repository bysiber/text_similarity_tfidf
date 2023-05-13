from sklearn.feature_extraction.text import TfidfVectorizer
import math


vectorizer = TfidfVectorizer()

# TF-IDF calculation
def get_tfidf_matrix(documents):
    tfidf_matrix = vectorizer.fit_transform(documents)
    return tfidf_matrix