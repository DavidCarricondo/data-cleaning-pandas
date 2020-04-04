### Function for cleaning pandas:

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
        r = re.search(r"\d{1,2}(?=h|:|\d{2})", e)
        if r:
            l.append(r.group())
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
    
#Function to categorize activity into 5 categories:

def fixactiv(lst):
    l = []
    for e in lst:
        if any(x in e.lower() for x in ['surf', 'boar','padd','kay']):
            l.append('surfing')
        elif any(x in e.lower() for x in ['spear', 'fish','hunt']):
            l.append('fishing')
        elif any(x in e.lower() for x in ['swim', 'snork', 'scub','div','bath','float','jump','play']):
            l.append('swimming')
        elif any(x in e.lower() for x in ['wading', 'stand', 'walk', 'sit','wash','splash']):
            l.append('standing')
        else: l.append('other')
    return l

##Function to extract country hemisphere. This function just uses countryinfo module 
#  to check whether the latitude of a country is positive or negative:

def hemis(x):
    try:
        if cti.CountryInfo(x).latlng()[0]>0:
            return 'N'
        else: return 'S'
    except: return None


#Function to calculate the percentage of fatal attacks over non-fatals (fatality):
def fatality(lst):
    l = list(lst)
    return (l.count('Y')/len(l))*100
