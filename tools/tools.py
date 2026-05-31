from core.state import STATE
import re
from collections import Counter

def update_essay(text: str):
    STATE["user_essay"] = text

def common_word_counter():
    words = re.findall(r'\b\w+\b', STATE["user_essay"].lower())
    word_counts = Counter(words)
    return word_counts.most_common(3)

def sentence_counter():
    sentences = re.findall(r'[^.!?]+[.!?]', STATE["user_essay"])
    return len(sentences)
