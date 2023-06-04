import string
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer

class accuracyClass:

    def calculate_accuracy(question, answer):
        # Tokenize and preprocess the question and answer
        stop_words = set(stopwords.words('english'))
        stemmer = PorterStemmer()

        question_tokens = word_tokenize(question.lower())
        question_tokens = [stemmer.stem(token) for token in question_tokens if token not in string.punctuation and token not in stop_words]

        answer_tokens = word_tokenize(answer.lower())
        answer_tokens = [stemmer.stem(token) for token in answer_tokens if token not in string.punctuation and token not in stop_words]

        # Calculate the accuracy score as the Jaccard similarity coefficient between the question and answer tokens
        intersection = set(question_tokens).intersection(set(answer_tokens))
        union = set(question_tokens).union(set(answer_tokens))
        accuracy = len(intersection) / len(union)

        return accuracy
    



