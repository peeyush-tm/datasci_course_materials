import sys
import json

import re

def only_letters(tested_string):
    match = re.match("^[A-Za-z]*$", tested_string)
    return match is not None


def score_tweet(tweet, scores):
    return sum(scores.get(word, 0) for word in tweet)


def read_scores(sent_file):
    with open(sent_file) as f:
        return {line.split('\t')[0]: int(line.split('\t')[1]) for line in f}


def unknown_word_scores(tweet_file, scores):
    with open(tweet_file) as f:
        tweets = (json.loads(line).get('text', '').split() for line in f)
        return {word: score_tweet(tweet, scores) / len(tweet)
                for tweet in tweets if tweet
                for word in tweet if word not in scores}

def lines(fp):
    print str(len(fp.readlines()))


def get_scores(afinnfile):
    
    scores = {} # initialize an empty dictionary
    for line in afinnfile:
        term, score  = line.split("\t")  # The file is tab-delimited. "\t" means "tab character"
        scores[term] = int(score)  # Convert the score to an integer.

    return scores


def main():
    sent_file = open(sys.argv[1])
    tweet_file = open(sys.argv[2])

    scores = read_scores(sent_file=sys.argv[1])

    sys.stdout.writelines('{0} {1}\n'.format(word.encode('utf-8'), score)
                          for word, score in unknown_word_scores(
                              tweet_file=sys.argv[2],
                              scores=scores).items())


if __name__ == '__main__':
    main()
