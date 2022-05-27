#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from pathlib import Path
import streamlit as st


# In[2]:


def clean_text(amount):
    dictionary = {"B":"000",'$':None,'M': None,'.':None,',':None}
    clean = amount.maketrans(dictionary)
    amount=amount.translate(clean)
    return amount


# In[5]:


chines_lend_path = Path(__file__).parents[0] /'chinese debt trap all over the world. - projects.csv'
china_lend_sector_path = Path(__file__).parents[0] /'chinese debt trap in Africa (sector wise).csv'


# In[ ]:


@st.cache(allow_output_mutation=True)
def load_data():
    #importing files
    china_lend=pd.read_csv(chines_lend_path)
    china_lend_sector = pd.read_csv(china_lend_sector_path)
    china_lend['AMOUNT']=china_lend['AMOUNT'].apply(lambda x: clean_text(x))
    china_lend_sector['$ Allocation'] = china_lend_sector['$ Allocation'].apply(lambda x: clean_text(x))
    china_lend['AMOUNT']=china_lend['AMOUNT'].astype(int)
    china_lend_sector['$ Allocation'] = china_lend_sector['$ Allocation'].astype(int)
    return china_lend,china_lend_sector


# In[ ]:


china_lend,china_lend_sector= load_data()
china_lend.isnull().sum()
china_lend_sector.isnull().sum()


# In[ ]:


#previewing files
ADD_Sidebar=st.sidebar.selectbox('CHINA LENDINGS OR AFRICAN COUNTRIES',('China lending Analysis','African debt Analysis'))


# In[6]:





# In[ ]:





# In[ ]:


china_lend['YEAR']=china_lend['YEAR'].astype(str)


# In[ ]:


#China's lending
if ADD_Sidebar == 'China lending Analysis':
    #summing up Amount by Years
    Amtyr=china_lend[['YEAR','AMOUNT']]
    Amtry =Amtyr.groupby('YEAR')['AMOUNT'].agg(sum).reset_index()#grouping data
    Amtry= pd.DataFrame(Amtry)
    # barplot showing how much China has spent each year
    fig,ax = plt.subplots()
    ax=sns.barplot(x='YEAR',y='AMOUNT',data=Amtry).set_title("China's lendings worldwide:Amount in millions of Dollars")
    st.pyplot(fig)
    filt=china_lend[china_lend['Country'].isin(china_lend_sector['Country'])]
    Africa=filt[['YEAR','AMOUNT']]
    Africa=Africa.groupby('YEAR')['AMOUNT'].agg(sum).reset_index()
    # barplot showing how much China has spent each year in Africa
    fig, ax = plt.subplots()
    ax=sns.barplot(x='YEAR',y='AMOUNT',data=Africa).set_title("china's lending to African countries::Amount in millions of Dollars")
    plt.show()
    st.pyplot(fig)
    others=china_lend[~china_lend['Country'].isin(china_lend_sector['Country'])]
    other=others[['YEAR','AMOUNT']]
    other=others.groupby('YEAR')['AMOUNT'].agg(sum).reset_index()
    # barplot showing how much China has spent each year in non-Africa
    fig, ax = plt.subplots()
    ax=sns.barplot(x='YEAR',y='AMOUNT',data=other).set_title("China's lending to non-African countries::Amount in millions of Dollars")
    plt.show()
    st.pyplot(fig)
    
    others_topCountries=others[['Country','AMOUNT']]
    others_topCountries=others_topCountries.groupby('Country')['AMOUNT'].agg(sum).reset_index()
    others_topCountries=others_topCountries.sort_values('AMOUNT')
    top_10=others_topCountries[-5:]
    Africa_top=filt[['Country','AMOUNT']]
    Africa_top = Africa_top.groupby('Country')['AMOUNT'].agg(sum).reset_index()
    Africa_top = Africa_top.sort_values('AMOUNT')
    A_top10=Africa_top[-5:] 
    frames=[top_10,A_top10]
    top_debtors=pd.concat(frames)
    #"china's top 5 debtors in other countries and top 5 debtors in Africa
    fig, ax = plt.subplots()
    ax= sns.barplot(x='Country',y='AMOUNT',data=top_debtors)
    ax.set_xticklabels(ax.get_xticklabels(),rotation=40, ha='right')
    ax.set_title("china's top 5 debtors in other countries and top 5 debtors in Africa::Amount in millions of Dollars ")
    st.pyplot(fig)
    plt.show()


# In[ ]:


if ADD_Sidebar == 'African debt Analysis':
    inv_sector=china_lend_sector[['Invested On','$ Allocation']]
    inv_sector=inv_sector.groupby('Invested On')['$ Allocation'].agg(sum).reset_index()
    fig, ax = plt.subplots()
    ax= sns.barplot(x='Invested On',y='$ Allocation',data=inv_sector)
    ax.set_xticklabels(ax.get_xticklabels(),rotation=90, ha='right')
    ax.set_title("Sectors of China's investments in Africa")
    st.pyplot(fig)
    plt.show()
    sectors=china_lend_sector[['Country','$ Allocation','Invested On']]
    #selecting Videos from Selectbox
    Country_select = sectors['Country'].value_counts()
    Country = tuple(Country_select.index)
    Country_select = st.selectbox('pick A Video',Country)
    Country_names= sectors[sectors['Country']==  Country_select]
    for country in Country_names['Country']:
        countries=(sectors['Country']==country)
        show_sectors=sectors.loc[countries,['Invested On','$ Allocation']]
        show_sectors=show_sectors.groupby('Invested On')['$ Allocation'].agg(sum).reset_index()
        fig, ax = plt.subplots()
        ax= sns.barplot(x='Invested On',y='$ Allocation',data=show_sectors)
        ax.set_xticklabels(ax.get_xticklabels(),rotation=90, ha='right')
        ax.set_title(f"{country}")
    st.pyplot(fig)
    plt.show()


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




