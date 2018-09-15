import re
import urllib.request
import time
from tkinter import Tk
from time import sleep
#https://www.dictionary.com/browse/
def getMeaning(word):
    url = "https://www.dictionary.com/browse/"+word
    objt = urllib.request.urlopen(url)
    data = objt.read()
    data1 = data.decode("utf-8")
    m = re.search('meta name="description" content="', data1)
    start = m.end()
    end = start + 400
    q = re.search("See more",data1[start:end])
    if q == None:
        return word+": Not Found"
    data1 = data1[start:start+q.start()]
    return data1
r = Tk()
r.withdraw()
prev = ""
while True:
    result = r.selection_get(selection="CLIPBOARD")
    if(result == prev):
        continue
    meaning = getMeaning(result)
    print(meaning+"\n")
    prev = result
    time.sleep(1)
