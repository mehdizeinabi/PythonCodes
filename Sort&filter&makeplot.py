#!/usr/bin/env python
# coding: utf-8

# In[1]:


import bamboolib as bam
import pandas as pd
df = pd.read_csv('C:/Users/lenovo/Desktop/import85.csv')
import pandas as pd; import numpy as np
# Step: Drop columns
df = df.drop(columns=['Unnamed: 0'])

# Step: Drop columns
df = df.drop(columns=['symboling'])

# Step: Drop columns
df = df.drop(columns=['normalized-losses'])

df


# In[2]:


import pandas as pd; import numpy as np
# Step: Drop rows where bore is missing
df = df.loc[~(df['bore'].isna())]


import pandas as pd; import numpy as np
# Step: Drop rows where num-of-doors is missing
df = df.loc[~(df['num-of-doors'].isna())]

# Step: Drop rows where horsepower is missing
df = df.loc[~(df['horsepower'].isna())]

df


# In[ ]:





# In[3]:


import plotly.express as px
fig = px.pie(df, names='fuel-type')
fig


# In[5]:


import pandas as pd; import numpy as np
# Step: Sort column(s) price ascending (A-Z)
df = df.sort_values(by=['price'], ascending=[True])

# Step: Sort column(s) make ascending (A-Z)
df = df.sort_values(by=['make'], ascending=[True])

# Step: Sort column(s) price ascending (A-Z)
df = df.sort_values(by=['price'], ascending=[True])

# Step: Sort column(s) fuel-type ascending (A-Z)
df = df.sort_values(by=['fuel-type'], ascending=[True])

import plotly.express as px
fig = px.histogram(df, x='make', y='price')
fig


# In[ ]:




