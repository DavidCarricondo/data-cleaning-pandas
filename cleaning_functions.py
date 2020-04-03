### Function for cleaning pandas:

##Column names to lower case removing blank spaces:

def fixcolnames(lst):
    l=[]
    for e in lst:
        x = e.replace(' ', '')
        l.append(x.lower())
    return l


##Function to fix the time column

##Function to classify night time

##Function to fix activity

#Function to fix life