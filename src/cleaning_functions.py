### Functions for cleaning pandas shark dataset:

#dependencies:

import re
import countryinfo as cti #https://pypi.org/project/countryinfo/


##Column names to lower case removing blank spaces from beginning and end and subituttin them by _ in the middle,
# it also removes comments between brackets after the name of the column:

def fixcolnames(lst):
    l=[]
    for e in lst:
        x = e.split('(') [0]
        x = x.strip(' ').replace(' ', '_')
        l.append(x.lower())
    return l


##Function to fix the time column. Extract the time for those values that provide a time
# otherwise, leave the string untouched:

def fixtime(lst):
    l = []
    for e in lst:
        r = re.search(r"\d{1,2}(?=[a-z]|:|\d{2})", e)
        if r:
            l.append(r.group())
        else: l.append(e)
    return l


##Function to classify night time.
# Times later than 20 and earlier than 8 are assign as night, if a text,
# some key words might indicate whether is night or day, otherwise none.

def timeclassify(lst):
    l = []
    dict = {'Night' : ['night', 'midnight', 'evening', 'dark', 'dusk', 'sunset', 'dawn', 'dusk', 'sundown'],
            'Day' : ['midday', 'afternoon', 'morning', 'noon', 'day', 'lunch']}
    for i, e in enumerate(lst):
        try:
            if int(e) > 20 or int(e)< 8:
                l.append('Night')
            else: l.append('Day')
        except:
            for k in dict.keys():
                if any(x in e.lower() for x in dict[k]):
                    l.append(k)
                    break
            if len(l) == i: l.append(None)
    return l
    
#Function to categorize activity into 5 categories:
# Categorizes activity if some keywords are detected in the text, else 'other'.

def fixactiv(lst):
    dict = {'fishing':['spear', 'fish','hunt'],
            'surfing':['surf', 'boar','padd','kay'],
            'swimming':['swim', 'snork', 'scub','div','bath','float','jump','play'],
           'standing':['wading', 'stand', 'walk', 'sit','wash','splash']}
    l = []
    for e in lst:
        for k in dict.keys():
            if any(x in e.lower() for x in dict[k]):
                l.append(k)
                break
        else: l.append('other')
    return l


#Function to calculate the percentage of fatal attacks over non-fatals (fatality):

def fatality(lst):
    l = list(lst)
    return (l.count('Y')/len(l))*100


##Functions for the bonus part:

#Function to fix the country column. 
# It splits a name if some non alphabetical or numerical simbols are present, 
# removes spaces from the edges, and convert them to lowercase

def fixcountry(x):
    try:
        s = re.search(r".*(?=[\/\(&\?,])",x)
        st = s.group()
        return st.strip(' ').lower()
    except: return x.strip(' ').lower()


#Function to extract the population of a country.
# Extract the population after converting the string into a CountryInfo object. 

def getpop(x):
    try:
        return cti.CountryInfo(x).population()
    except: return None