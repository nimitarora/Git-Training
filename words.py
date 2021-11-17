from urllib.request import urlopen

def fetch_words():
    story = urlopen('http://sixty-north.com/c/t.txt')
    story_words = []

    for line in story:
        line_words = line.decode('utf-8').split()
        for words in line_words:
            story_words.append(words)

    story.close()

    for word in story_words:
        print(word)

if __name__ == '__main__':
    fetch_words()


