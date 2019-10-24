
# coding: utf-8

# In[97]:

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
oil = pd.read_csv("oil_reserves.csv")
oil = oil.fillna(0)
oil

#df = oil['2010']+oil['2011']+oil['2012']+oil['2013']+oil['2014']+oil['2015']+oil['2016']
#df


# In[100]:

#Which region has max oil reserves from 2014 to 2016?
max_t = oil['2014']+oil['2015']+oil['2016']
max_t.max()





# In[65]:

oil['2010'],oil['2011'],oil['2012'],oil['2013'],oil['2014'],oil['2015'],oil['2016'].plot(kind="bar", figsize=(15,7), color="#61d199")
#oil['2011'].plot(kind = "bar",flagsize=(15,7),color ="#61d199")
plt.show()


# In[72]:

oil["2010"] = oil["2010"] + oil["2011"]+oil["2012"]+oil["2013"]+oil["2014"]+oil["2015"]+oil["2016"]
regions=oil.sort_values("2010",ascending=False).head(3)
regions["Country/ Region"]


# In[87]:

#Draw suitable visualization which shows the share of oil reserves by each region.
North_america = oil['2010']+oil['2011']+oil['2012']+oil['2013']+oil['2014']+oil['2015']+oil['2016']
South_central = oil['2010'] + oil['2012']+oil['2013']+oil['2014']+oil['2015']+oil['2016']
Asia_pacific =  oil['2010'] + oil['2012']+oil['2013']+oil['2014']+oil['2015']+oil['2016']
middle_east =  oil['2010'] + oil['2012']+oil['2013']+oil['2014']+oil['2015']+oil['2016']
africa =  oil['2010'] + oil['2012']+oil['2013']+oil['2014']+oil['2015']+oil['2016']
Europe =  oil['2010'] + oil['2012']+oil['2013']+oil['2014']+oil['2015']+oil['2016']
plt.bar(North_america,height = 0.8,width = 0.8)
#['2010'].plot(kind="bar", figsize=(15,7), color="#61d199")


# In[93]:

#Find the world’s top 5 countries having maximum oil reserves in the 2015. Show their % of share in total oil reserve for the same year.
oil['2015'].max()
#oil[Country/ Region].max()


# In[112]:

#Draw any type of visualizations you know
plt.scatter(oil['2010'],oil['2011'],color ='red')
plt.show()


# 

# In[113]:

plt.scatter(oil['2011'],oil['2012'],color ='red')
plt.show()


# In[115]:

plt.scatter(oil['2012'],oil['2014'],color ='green')
plt.show()


# In[ ]:

plt.subplot()

