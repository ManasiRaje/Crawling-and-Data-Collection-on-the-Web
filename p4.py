import urllib
import httplib
import json
import datetime, time
import pprint
        
#########   create UNIX timestamps
start_date = datetime.datetime(2015,02,01, 20,0,0)
end_date = datetime.datetime(2015,02,02, 11,0,0)
mintime = int(time.mktime(start_date.timetuple()))
maxtime = int(time.mktime(end_date.timetuple()))

API_KEY = '09C43A9B270A470B8EB8F2946A9369F3'
host = 'api.topsy.com'
url = '/v2/content/citations.json'

f = open(r'C:\Users\Manasi\Documents\Winter2015\ee239\Project 2\q3\SNL\citations_SNL.txt', 'w+')
# let us set time-window to 60 seconds
step = 600
#for x in my_range(mintime, maxtime, step):
for x in range(mintime, maxtime, step):
    start_time = x
    end_time = x + step
    #########   set query parameters
    params = urllib.urlencode({'apikey' : API_KEY, 'q' :'#SNL',
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
    citations = ret['response']['results']['latest_post']

    # write them into top_tweets.txt
    #for x in citaions.get('tweet').get('retweet_count')
    #    f.write(str((x.get('tweet').get('text')).encode("utf-8")))
    #    f.write('\n')
    pprint.pprint(citations)
f.close()
