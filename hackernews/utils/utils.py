import re

def word_count(title):
    words = re.findall(r'\b\w+(?:-\w+)*\b', title)
    return len(words)