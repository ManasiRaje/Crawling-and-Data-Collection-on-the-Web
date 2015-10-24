import urllib
import httplib
import json
import datetime, time
import pprint

# function to increment loop iterator by a certain step
# def my_range(start, end, step):
#    while (start + step) < end:
#        yield start
#        start += step
        
#########   create UNIX timestamps
start_date = datetime.datetime(2015,02,01, 20,0,0)
end_date = datetime.datetime(2015,02,02, 11,0,0)
mintime = int(time.mktime(start_date.timetuple()))
maxtime = int(time.mktime(end_date.timetuple()))

API_KEY = '09C43A9B270A470B8EB8F2946A9369F3'
host = 'api.topsy.com'
url = '/v2/content/tweets.json'

f2 = open(r'C:\Users\Manasi\Documents\Winter2015\ee239\Project 2\q2\search_log.txt', 'w+')
# let us set time-window to 600 seconds
step = 600
t = 1
#for x in my_range(mintime, maxtime, step):
for x in range(mintime, maxtime, step):
    start_time = x
    end_time = x + step
    #########   set query parameters
    params = urllib.urlencode({'apikey' : API_KEY, 'q' :'#Colts',
                           'mintime': str(start_time), 'maxtime': str(end_time),
                           'include_metrics':'1', 'limit': 500})

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

    # write them into top_tweets.txt
    f1 = open(r'C:\Users\Manasi\Documents\Winter2015\ee239\Project 2\q2\tweets' + str(t) +'.txt', 'w+')
    for x in tweets:
        f1.write(str(x.get('tweet')))
        f1.write('\n\n\n')
    f1.close()
    t += 1

    # write the number of tweets in this slot into the log file
    d_start = datetime.datetime.fromtimestamp(start_time)
    d_end = datetime.datetime.fromtimestamp(end_time)
    f2.write('#Colts\tFrom: ' + str(d_start) + '\tTo: ' + str(d_end) +'\tNo. of Results: ' + str(len(tweets)) + '\n')

f2.close()

    

        
