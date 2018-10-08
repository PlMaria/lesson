import urllib.request
import re

def get_url_count(url):
    t=0
    with urllib.request.urlopen(url) as webpage:
        for line in webpage:
           line = line.strip()
           line = line.decode('utf-8')
           r=re.findall('http(s)?://',line)
           s=len(r)
           t=t+s
    return t

#print(get_url_count("https://dfedorov.spb.ru/python3/"))

'''
19
'''

def get_url_count1(url):
    t=0
    try:
        with urllib.request.urlopen(url) as webpage:
            text=webpage.read().decode('utf-8')
           
        r=re.findall('http(s)?://',text)
        t=len(r)
        return t
    
    except Exception as e:
        return e

#print(get_url_count1("https://dfedorov.spb.ru/python3/"))

if __name__=='__main__':
    url="https://dfedorov.spb.ru/python3/"
    print(get_url_count(url))
    print(get_url_count1(url))
