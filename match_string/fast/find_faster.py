# TODO: change the find function so that it looks through `text` more
# systematically, that it returns `-1` if `word` cannot be found.

from random import randrange

def find_faster(word: str, text: str) -> int:
    """Find a word in a string."""
    word_len = len(word)
    text_len = len(text)
    found = False
    if word_len <= 1:
        for i in range(text_len):
            if text[i : i + word_len] == word:
                found = True
                break
    elif word_len > 1:
        for i in range(text_len - word_len + 1):
            if text[i] == word[0]:
                if text[i+1 : i + word_len] == word[1:]:
                    found = True
                    break
    return i if found else -1

# with open("/Users/temporaryadmin/github-classroom/dci-dh-python-e21-01/python-algorithmic_thinking-algorithm_efficiency-SyncopatedPandemonium/src/sample.txt") as f:
#     sample_text = f.read()

# print(find_faster(".", sample_text))
