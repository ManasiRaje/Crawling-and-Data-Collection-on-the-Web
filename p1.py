import urllib
import httplib
import json
import datetime, time
import pprint

#f1 = open('C:\Users\Manasi\Documents\Winter2015\ee239\Project 2\demo.py', 'r')
#f1.read()

#f2 = open(r'C:\Users\Manasi\Documents\Winter2015\ee239\Project 2\tweets.txt', 'r')
#f2.read()

#########   create UNIX timestamps
start_date = datetime.datetime(2015,02,01, 20,0,0)
end_date = datetime.datetime(2015,02,02, 11,0,0)
mintime = int(time.mktime(start_date.timetuple()))
maxtime = int(time.mktime(end_date.timetuple()))

API_KEY = '09C43A9B270A470B8EB8F2946A9369F3'
host = 'api.topsy.com'
url = '/v2/content/tweets.json'

#########   set query parameters
params = urllib.urlencode({'apikey' : API_KEY, 'q' :'#Colts',
                           'mintime': str(mintime), 'maxtime': str(maxtime), 'limit': 2})  #,
                           # default limit is 5
                           #'new_only': '1', 'include_metrics':'1', 'limit': 5})


#########   create and send HTTP request
req_url = url + '?' + params
req = httplib.HTTPConnection(host)
req.putrequest("GET", req_url)
req.putheader("Host", host)
req.endheaders()
req.send('')


#########   get response and print out status
resp = req.getresponse()
print resp.status, resp.reason


#########   extract tweets
resp_content = resp.read()
ret = json.loads(resp_content)
tweets = ret['response']['results']['list']

#print tweets
#tweets[1].get('author').get(u'name')

# print tweets using pprint
pprint.pprint(tweets)
raw_input('Press enter to continue...')

# write them into top_tweets.txt
f = open(r'C:\Users\Manasi\Documents\Winter2015\ee239\Project 2\q6\top_tweets.txt', 'w+')
for x in tweets:
    f.write(str(x.get('tweet')))
    f.write('\n\n\n')
f.close()

# write answer for the report
f = open(r'C:\Users\Manasi\Documents\Winter2015\ee239\Project 2\q6\tweets_for_report.txt', 'w+')
for x in tweets:
    f.write('User : ' + str(x.get('tweet').get('user').get('name')) + '\n')
    f.write('Text : ' + str(x.get('tweet').get('text')) + '\n')
    #d = datetime.datetime.fromtimestamp(x.get('firstpost_date')).strftime("%B %d, %Y")
    d = datetime.datetime.fromtimestamp(x.get('firstpost_date'))
    f.write('Date : ' + str(d) + '\n')
    f.write('\n\n\n')
f.close()

        
