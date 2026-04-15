import re

def extract_patterns(text, pattern_type):
    results = [] 
    
    email_re = re.compile(r"\b[\w.\-+]+@(?:[\w-]+\.)+[a-zA-Z]{2,}\b")
    urls_re = re.compile(r'https?://[\S]+(?<![.,?!])')

    dates_re = re.compile(r'\b(?:\d{1,2}/\d{1,2}/\d{2,4}|\d{4}[-/]\d{1,2}[-/]\d{1,2})\b')
    money_re = re.compile(r'\$\d+(?:\.\d{2})?')
    hashtags_re = re.compile(r"#\w+")

    if pattern_type == "emails":
        results = email_re.findall(text)
    elif pattern_type == "urls":
        results = urls_re.findall(text)
    elif pattern_type == "dates":
        results = dates_re.findall(text)
    elif pattern_type == "money":
        results = money_re.findall(text)
    elif pattern_type == "hashtags":
        results = hashtags_re.findall(text)
        
    return results