import os, sys
import collections
import glob
import re

WORD = re.compile(r"\w{3,}")
def read_word_chains(filepath):
    with open(filepath, encoding="utf-8") as f:
        for i in WORD.finditer(f.read()):
            yield i.group().lower()

words = []
for filepath in glob.glob("*.txt"):
    print(filepath)
    words.extend(read_word_chains(filepath))

word_counts = collections.defaultdict(collections.Counter)
for w1, w2 in zip(words[:-1], words[1:]):
    counter = word_counts[w1]
    counter[w2] += 1

if __name__ == '__main__':
    word = input("Starting word: ").lower()
    sentence = []
    for i in range(7):
        sentence.append(word)
        for (word, count) in word_counts[word].most_common(1):
            break

    print(" ".join(sentence))