import nltk
from nltk.translate.bleu_score import sentence_bleu


class bleauClass:
    def calculate_bleu_score(question, answer, context):
        # Tokenize the question, answer, and context
        question_tokens = nltk.word_tokenize(question.lower())
        answer_tokens = nltk.word_tokenize(answer.lower())
        context_tokens = nltk.word_tokenize(context.lower())

        # Calculate the BLEU score
        weights = [1.0 / n for n in range(1, 5)]  # Use weights for up to 4-grams
        bleu_score = sentence_bleu([question_tokens, context_tokens], answer_tokens, weights=weights)
    
        return bleu_score
    


