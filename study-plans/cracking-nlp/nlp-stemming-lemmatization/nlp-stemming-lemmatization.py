from nltk.stem import WordNetLemmatizer
import nltk
def stem_and_lemmatize(word, lemma_dict):
    p = {}

    def clean(t):
        s = word

        if s.endswith("ing") and len(s) - 3 >= 3:
            s = s[:-3]

       
        elif s.endswith("ly") and len(s) - 2 >= 3:
            s = s[:-2]

     
        elif s.endswith("ed") and len(s) - 2 >= 3:
            s = s[:-2]

        
        elif s.endswith("s") and not s.endswith("ss") and len(s) - 1 >= 2:
            s = s[:-1]

        
        elif s.endswith("er") and len(s) - 2 >= 3:
            s = s[:-2]

        #
        elif s.endswith("tion") and len(s) - 4 + 2 >= 3:
            
            s = s[:-4] + "te"

        return s

    stem = clean(word)
    p["stem"] = stem
    # nltk.download('wordnet')
    # l= WordNetLemmatizer().lemmatize(word)
    # if l not in lemma_dict:
    #     lemma_dict[word]=l
    p["lemma"] = lemma_dict.get(word,word)

    return p