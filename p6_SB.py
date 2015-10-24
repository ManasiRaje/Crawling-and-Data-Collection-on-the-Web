ht = '#SuperBowl'
result = open(r'C:\Users\Manasi\Documents\Winter2015\ee239\Project 2\archana\\' + ht + '\parser_results_' + ht + '.txt', 'w')
for t in range(1,901):
    rest = ht + '\\tweets' + str(t) + '.txt'
    print rest
    f = open(r'C:\Users\Manasi\Documents\Winter2015\ee239\Project 2\archana\\' + rest, 'r')
    f_list = f.read()
    f_list = json.loads(f_list)
    for x in f_list:
        dict_tweet = x
        d = datetime.datetime.fromtimestamp(dict_tweet.get('firstpost_date'))
        result.write('Post date: ' + str(d) + '\n')
        result.write('Text: ' + (dict_tweet.get('tweet').get('text')).encode('utf-8').strip() + '\n')
        result.write('Number of retweets: ' + str(dict_tweet.get('tweet').get('retweet_count')) + '\n')
        result.write('User: ' + (dict_tweet.get('tweet').get('user').get('name')).encode('utf-8').strip() + '\n\n\n')
    f.close()
result.close()
