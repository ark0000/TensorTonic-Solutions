import re

def text_normalize(text, operations):
    v=text
    for i in operations:
        if i=="lowercase":
            v=v.lower()
        if i=="remove_punctuation":
            v=re.sub("[^a-zA-Z0-9\s]*","",v)
        if i=="remove_digits":
            v=re.sub("\d+","",v)
        if i=="collapse_whitespace":
            v=re.sub("\s{2,}"," ",v)
        if i=="strip":
            v=v.strip()
    return v
    
    """
    Returns: str
    """
   