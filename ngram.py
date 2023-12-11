from nltk import ngrams

from nltk.util import ngrams
#unigram model
n = 1
sentence = 'Artificial intelligence (AI) is the intelligence of machines or software, as opposed to the intelligence of humans or animals. It is a field of study in computer science that develops and studies intelligent machines. "AI" may also refer to the machines themselves.'
unigrams = ngrams(sentence.split(), n)
print("Unigram : ")
for item in unigrams:
    print(item)
#bigram model
n = 2
sentence = 'Artificial intelligence (AI) is the intelligence of machines or software, as opposed to the intelligence of humans or animals. It is a field of study in computer science that develops and studies intelligent machines. "AI" may also refer to the machines themselves.'
unigrams = ngrams(sentence.split(), n)
print("\nBigram : ")
for item in unigrams:
    print(item)
#trigram model
n = 3
sentence = 'Artificial intelligence (AI) is the intelligence of machines or software, as opposed to the intelligence of humans or animals. It is a field of study in computer science that develops and studies intelligent machines. "AI" may also refer to the machines themselves.'
unigrams = ngrams(sentence.split(), n)
print("Trigram : ")
for item in unigrams:
    print(item)

#using text file input
from nltk import ngrams
file = open("/home/exam/Desktop/NLP_Lab_AVG/AI.txt")
for i in file.readlines():
    cumulative = i
    sentences = i.split(".")
    counter = 0
    print("\nUsing Text File : ")
    for sentence in sentences:
        print("For sentence", counter + 1, ", trigrams are: ")
        trigrams = ngrams(sentence.split(" "), 3)
        for grams in trigrams:
            print(grams)
        counter += 1
        print()
