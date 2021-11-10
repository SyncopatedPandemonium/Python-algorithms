#!/usr/bin/env python

import random
import time
import re

from find_faster import find_faster

def main_faster():
    with open("/Users/temporaryadmin/github-classroom/dci-dh-python-e21-01/python-algorithmic_thinking-algorithm_efficiency-SyncopatedPandemonium/src/sample.txt") as f:
        sample_text = f.read()
    words = re.split("\s|(?<!\d)[,.](?!\d)", sample_text)
    index_error = False
    timer = 0
    for i in range(0, 10000):
        word = random.choice(words)
        start = time.perf_counter()
        index = find_faster(word, sample_text)
        end = time.perf_counter()
        timer = timer + end - start
        index_control = [_.start() for _ in re.finditer(word, sample_text)]
        if index not in index_control:
            index_error = True
            print({"word": word, "index": index, "index_control": index_control})
    if index_error:
        print(
            "Unfortunately your algorithm did not always find the correct index number."
        )
    else:
        print("Congratulations, your algorithm always found the word correctly.")
        print(f"It only took {timer} seconds to run it 10000 times.")


if __name__ == "__main__":
    main_faster()