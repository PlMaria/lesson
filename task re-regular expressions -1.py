import urllib.request
import re

def get_url_count(url):
    with urllib.request.urlopen(url) as webpage:
        for line in webpage:
            r=re.compile(r'http(s)?://')
            t=0
            try:
                r.search('http(s)?://').group()
                t=t+1
            except:
                continue

    return t

#print(get_url_count("https://dfedorov.spb.ru/python3/"))

def get_url_count1(url):
    t=0
    with urllib.request.urlopen(url) as webpage:
        for line in webpage:
           line = line.strip()
           line = line.decode('utf-8')
           r=re.findall('http(s)?://',line)
           s=len(r)
           t=t+s
    return t

print(get_url_count1("https://dfedorov.spb.ru/python3/"))

'''
19
'''
