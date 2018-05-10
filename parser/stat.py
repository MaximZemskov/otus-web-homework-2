import collections
import re


def calculate_word_frequency_stat(articles_info, min_word_len=3):
    words = []

    lower_letters_regex = re.compile('[^a-zа-я]')
    for article_info in articles_info:
        words_string = '%s %s' % (
            article_info['title'],
            article_info['preview'],
        )
        words_string = words_string.lower().strip()
        current_words = lower_letters_regex.sub(
            ' ',
            words_string
        ).split()
        words += [w.strip() for w in current_words if w and len(w) >= min_word_len]
    return collections.Counter(words).most_common()


def output_word_stat(word_stat, top_size=10):
    for word, repetitions_amount in word_stat[:top_size]:
        print('%s: %s' % (word, repetitions_amount))