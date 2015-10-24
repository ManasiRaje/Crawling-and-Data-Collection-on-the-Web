from os import path
import json
import datetime, time
import ast

hashtags = ['#Colts', '#DeflatedBalls', '#DeflateGate', '#NFL', '#SNL', '#SuperBowl']
for ht in hashtags:
    result = open(r'C:\Users\Manasi\Documents\Winter2015\ee239\Project 2\archana\\' + ht + '\parser_results_' + ht + '.txt', 'w')
    for hr in range(1,16):
        for t in range(1,61):
            file_no = (hr-1)*60 + t%60
            if t%60 == 0:
                file_no = (hr-1) * 60 + 60
            rest = ht + '\Hour' + str(hr) + '\\tweets' + str(file_no) + '.txt'
            print rest
            f = open(r'C:\Users\Manasi\Documents\Winter2015\ee239\Project 2\archana\\' + rest, 'r')
            f_list = f.readlines()
            for tweet_item in f_list:
                tweet_item = ast.literal_eval(tweet_item)
                tweet_item = json.loads(tweet_item)
                for x in tweet_item:
                    dict_tweet = x
                    d = datetime.datetime.fromtimestamp(dict_tweet.get('firstpost_date'))
                    result.write('Post date: ' + str(d) + '\n')
                    result.write('Text: ' + (dict_tweet.get('tweet').get('text')).encode('utf-8').strip() + '\n')
                    result.write('Number of retweets: ' + str(dict_tweet.get('tweet').get('retweet_count')) + '\n')
                    result.write('User: ' + (dict_tweet.get('tweet').get('user').get('name')).encode('utf-8').strip() + '\n\n\n')
                f.close()
    result.close()
