# TODO: change the find function so that it looks through `text` more
# systematically, that it returns `-1` if `word` cannot be found.

from random import randrange

def find(word: str, text: str) -> int:
    """Find a word in a string."""
    word_len = len(word)
    text_len = len(text)
    found = False
    while not found:
        i = randrange(text_len - word_len)
        if text[i : i + word_len] == word:
            found = True
    return i if True else -1

with open("/Users/temporaryadmin/github-classroom/dci-dh-python-e21-01/python-algorithmic_thinking-algorithm_efficiency-SyncopatedPandemonium/src/sample.txt") as f:
    sample_text = f.read()

print(find("dolor", sample_text))