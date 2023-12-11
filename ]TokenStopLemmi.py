import spacy
nlp = spacy.load("en_core_web_sm")
        
#Tokenization
print("\nTokenization :-")
about_text = (
    "Atharva is a Python developer currently"
    " working for a London-based Fintech"
    " company. He is interested in learning"
    " Natural Language Processing."
    )
about_doc = nlp(about_text)

for token in about_doc:
  print (token, token.idx)
  
#Stop words  
print("\nStop words :-") 
spacy_stopwords = spacy.lang.en.stop_words.STOP_WORDS
len(spacy_stopwords)
for stop_word in list(spacy_stopwords)[:10]:
    print(stop_word)
    custom_about_text = (
    "Atharva is a Python developer currently"
    " working for a London-based Fintech"
    " company. He is interested in learning"
    " Natural Language Processing."
    )
about_doc = nlp(custom_about_text)
print([token for token in about_doc if not token.is_stop])

#Lemmatization
print("\nLemmatization :-")
conference_help_text = (
    "Atharva is a Python developer currently"
    " working for a London-based Fintech"
    " company. He is interested in learning"
    " Natural Language Processing."
    )
conference_help_doc = nlp(conference_help_text)
for token in conference_help_doc:
    if str(token) != str(token.lemma_):
        print(f"{str(token):>20} : {str(token.lemma_)}")


#Part of Speech
print("\nPart of Speech :-")
about_text = (
    "Atharva is a Python developer currently"
    " working for a London-based Fintech"
    " company. He is interested in learning"
    " Natural Language Processing."
    )
about_doc = nlp(about_text)
for token in about_doc:
    print(
        f"""
TOKEN: {str(token)}
=====
TAG: {str(token.tag_):10} POS: {token.pos_}
EXPLANATION: {spacy.explain(token.tag_)}"""
    )
