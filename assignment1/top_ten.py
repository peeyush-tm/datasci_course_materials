import sys
import json
from collections import Counter


def get_top_ten(tweet_file):
    with open(tweet_file) as f:
        entities = (json.loads(line).get('entities', None) for line in f)
        tweet_hashtags = (entity.get('hashtags') for entity in entities if entity)
        texts = (tag['text'].encode('utf-8') for hashtags in tweet_hashtags for tag in hashtags)
        return Counter(texts).most_common(10)


if __name__ == '__main__':
    top_ten = get_top_ten(tweet_file=sys.argv[1])
    sys.stdout.writelines('{0} {1}.0\n'.format(*pair) for pair in top_ten)