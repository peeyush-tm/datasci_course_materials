import sys
import json

def hw(scores, tweet_lines):
    each_tweet_score = list()
    for tweet_line in tweet_lines:
        tweet = json.loads(tweet_line)
        tweet_text = tweet.get("text")
        if tweet_text:
            tweet_words = tweet_text.split(" ")
            tweet_score = 0
            for word in tweet_words:
                if word in scores:
                    tweet_score += scores.get(word)
            each_tweet_score.append(tweet_score)
    return each_tweet_score


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

    # read all the lines in the tweet file
    tweet_lines = tweet_file.readlines()
    
    scores = get_scores(sent_file)
    
    #close sent file
    sent_file.close()

    # close the file 
    tweet_file.close()

    tweet_scores = hw(scores, tweet_lines)

    for ts in tweet_scores:
        print ts

if __name__ == '__main__':
    main()
