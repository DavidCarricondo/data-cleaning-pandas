### Function for cleaning pandas:

#dependencies:

import re

##Column names to lower case removing blank spaces from beginning and end and subituttin them by _ in the middle:

def fixcolnames(lst):
    l=[]
    for e in lst:
        x = e.strip(' ').replace(' ', '_')
        l.append(x.lower())
    return l


##Function to fix the time column. Extract the time for those values that provide a time
# otherwise, leave the string untouched:

def fixtime(lst):
    l = []
    for e in lst:
        r = re.search(r"\d{1,2}(?=h|:|\d{2})", e).group()
        if r:
            l.append(r)
        else: l.append(e)
    return l


##Function to classify night time

def timeclassify(lst):
    l = []
    key_night = ['night', 'midnight', 'evening', 'dark', 'dusk', 'sunset', 'dawn', 'dusk', 'sundown']
    key_day = ['midday', 'afternoon', 'morning', 'noon', 'day', 'lunch']
    
    for e in lst:
        try:
            if int(e) > 20 or int(e)< 8:
                l.append('Night')
            else: l.append('Day')
        except:
            if any(x in e.lower() for x in key_night):
                l.append('Night')
            elif any(x in e.lower() for x in key_day):
                l.append('Day')
            else: l.append(None)
    return l
    

##Function to fix activity

#Function to fix life