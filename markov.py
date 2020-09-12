def is_alpha(word):
    letters = "abcdefghijklmnopqrstuvwxyz"
    return all(w in letters for w in word)

def words_from_file(filepath):
    word_list = []
    text_file = open(filepath, "r")
    text = text_file.read()[:4000]
    lines = text.splitlines()
    for line in lines:
        words_in_line = line.split()
        for word in words_in_line:
            word_list.append(word.lower())
    return word_list

def words_from_file2(filepath):
    for line in open(filepath):
        for word in line.split():
            yield word

def refined_words(words):
    """Only return words which consist entirely of letters
    """
    new_words = []
    for word in words:
        if word.isalpha() and len(word) > 3:
            new_words.append(word)
    return new_words

def refined_words2(words):
    for word in words:
        if not ... :
            yield word

def pairs_of_words(words):
    c = 0
    new_list = []
    while c < len(words) - 1:
        new_list.append((words[c], words[c + 1]))
        c += 1
    return new_list

def refined_words2(words):
    return [word for word in words if word.isalpha()]

if __name__ == '__main__':
    initial = words_from_file("bleak-house.txt")
    refined = refined_words(initial)
    pairs = pairs_of_words(refined)
    print(pairs)