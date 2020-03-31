import re
import joblib
import nltk

# The Classify function accepts a string and outputs a sentiment classification, the sentence string is cleaned of punctuation, digits and stopwords within the function.

def classify(sentence):
    classifier = joblib.load("model.pkl")

    def preprocessor(sentence):
        sentence = sentence.strip().lower()
        sentence = re.sub(r"\d+", "", sentence)
        sentence = re.sub(r'[^\w\s]', '', sentence)
        sentence = " ".join([w for w in nltk.word_tokenize(sentence) if len(w) > 1])

        return sentence

    clean_data = [preprocessor(sentence)]
    vec = joblib.load("vectorizer.pkl")
    data_text_sparse = vec.transform(clean_data)

    prediction = classifier.predict(data_text_sparse)[0]

    return prediction
