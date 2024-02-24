#!/usr/bin/env python
# coding: utf-8

# In[1]:


get_ipython().system('pip install selenium')

Q.1-Scrape the details of most viewed videos on YouTube from Wikipedia. Url
= https://en.wikipedia.org/wiki/List_of_most-viewed_YouTube_videos You need to find following details: 
# In[2]:


import selenium
import pandas as pd
from selenium import webdriver
import warnings
warnings.filterwarnings('ignore')
from selenium.webdriver.common.by import By
import time


# In[237]:


driver=webdriver.Chrome()
driver.get("https://en.wikipedia.org/wiki/List_of_most-viewed_YouTube_videos")


# In[240]:


names=[]
Artists=[]
upload_dates=[]
views=[]


# In[243]:


try:
    name_tags=driver.find_elements(By.XPATH,'//table[@class="sortable wikitable sticky-header static-row-numbers col3center col4right jquery-tablesorter"]/tbody/tr/td[1]')
    for i in name_tags[0:10]:
        name=i.text
        names.append(name)

    Artist_tags=driver.find_elements(By.XPATH,'//table[@class="sortable wikitable sticky-header static-row-numbers col3center col4right jquery-tablesorter"]/tbody/tr/td[2]')
    for i in Artist_tags[0:10]:
        Artist=i.text
        Artists.append(Artist)

    views_tags=driver.find_elements(By.XPATH,'//table[@class="sortable wikitable sticky-header static-row-numbers col3center col4right jquery-tablesorter"]/tbody/tr/td[3]')
    for i in views_tags[0:10]:
        view=i.text
        views.append(view)

    upload_dates_tags=driver.find_elements(By.XPATH,'//table[@class="sortable wikitable sticky-header static-row-numbers col3center col4right jquery-tablesorter"]/tbody/tr/td[4]')
    for i in upload_dates_tags[0:10]:
        upload_date=i.text
        upload_dates.append(upload_date)
    
except Exception as e:
    print("error:",str(e))

    


# In[244]:


import pandas as pd
pd.DataFrame({'names':names,'Artists':Artists,'upload_dates':upload_dates,'views':views})

Q.2-Scrape the details team India’s international fixtures from bcci.tv.
Url = https://www.bcci.tv/. 
# In[245]:


driver=webdriver.Chrome()
driver.get("https://www.bcci.tv/")


# In[246]:


designation1=driver.find_element(By.XPATH,'/html/body/header/div[3]/div[2]/ul/div[1]/a[2]')
designation1.click()


# In[247]:


Serieses=[]
Places=[]
Dates=[]
Times=[] 


# In[248]:


try:
    Series_tags=driver.find_elements(By.XPATH,'//div[@class="tags-wrap"]/span[1]')
    for i in Series_tags[0:6]:
        Series=i.text
        Serieses.append(Series)

    Place_tags=driver.find_elements(By.XPATH,'//div[@class="match-place ng-scope"]')
    for i in Place_tags[0:6]:
        Place=i.text
        Places.append(Place)


    Date_tags=driver.find_elements(By.XPATH,'//div[@class="match-dates ng-binding"]')
    for i in Date_tags[0:6]:
        Date=i.text
        Dates.append(Date)


    Time_tags=driver.find_elements(By.XPATH,'//div[@class="match-time no-margin ng-binding"]')
    for i in Time_tags[0:6]:
        Time=i.text
        Times.append(Time)
        
except Exception as e:
    print("error:",str(e))


# In[249]:


import pandas as pd
pd.DataFrame({'Serieses':Serieses,'places':Places,'Dates':Dates,'Times':Times})

Q.3-Scrape the details of State-wise GDP of India from statisticstime.com.
Url = http://statisticstimes.com/ 
# In[250]:


driver=webdriver.Chrome()
driver.get("http://statisticstimes.com/")


# In[251]:


designation1=driver.find_element(By.XPATH,'/html/body/div[2]/div[1]/div[2]/div[2]/button')
designation1.click()


# In[252]:


designation1=driver.find_element(By.XPATH,'/html/body/div[2]/div[1]/div[2]/div[2]/div/a[3]')
designation1.click()


# In[255]:


designation1=driver.find_element(By.XPATH,'/html/body/div[2]/div[2]/div[2]/ul/li[1]/a')
designation1.click()


# In[256]:


States=[]
GSDPs1=[]
GSDPs2=[]
Shares=[]
GDPs=[]
stateGDP=[]


# In[258]:


try:
    States_tags=driver.find_elements(By.XPATH,'//table[@id="table_id"]/tbody/tr/td[1]')
    for i in States_tags:
        State=i.text
        States.append(State)


    GSDPs1_tags=driver.find_elements(By.XPATH,'//table[@id="table_id"]/tbody/tr/td[2]')
    for i in GSDPs1_tags:
        GSDP1=i.text
        GSDPs1.append(GSDP1)


    GSDPs2_tags=driver.find_elements(By.XPATH,'//table[@id="table_id"]/tbody/tr/td[3]')
    for i in GSDPs2_tags:
        GSDP2=i.text
        GSDPs2.append(GSDP2)


    Share_tags=driver.find_elements(By.XPATH,'//table[@id="table_id"]/tbody/tr/td[4]')
    for i in Share_tags:
        Share=i.text
        Shares.append(Share)

    
    GDP_tags=driver.find_elements(By.XPATH,'//table[@id="table_id"]/tbody/tr/td[5]')
    for i in GDP_tags:
        GDP=i.text
        GDPs.append(GDP)



    GDPs_tags=driver.find_elements(By.XPATH,'//table[@id="table_id"]/tbody/tr/td[6]')
    for i in GDPs_tags:
        GDPss=i.text
        stateGDP.append(GDPss)
        
except Exception as e:
    print("error:",str(e))

    


# In[259]:


import pandas as pd
pd.DataFrame({'Rank':States,'GSDPs1':GSDPs1,'GSDPs2':GSDPs2,'Shares':Shares,'GDPs':GDPs,'stateGDP':stateGDP
})

Q.4-Scrape the details of trending repositories on Github.com.
Url = https://github.com/ 
# In[260]:


driver=webdriver.Chrome()
driver.get("https://github.com/")


# In[261]:


designation1=driver.find_element(By.XPATH,'/html/body/div[1]/div[1]/header/div/div[2]/div/nav/ul/li[3]/button')
designation1.click()


# In[262]:


designation1=driver.find_element(By.XPATH,'/html/body/div[1]/div[1]/header/div/div[2]/div/nav/ul/li[3]/div/div[3]/ul/li[2]/a')
designation1.click()


# In[263]:


titles=[]
descriptions=[]
counts=[]
languages=[] 


# In[265]:


try:
    titles_tags=driver.find_elements(By.XPATH,'//article[@class="Box-row"]/h2')
    for i in titles_tags:
        title=i.text
        titles.append(title)


    descriptions_tags=driver.find_elements(By.XPATH,'//p[@class="col-9 color-fg-muted my-1 pr-4"]')
    for i in descriptions_tags:
        description=i.text
        descriptions.append(description)



    counts_tags=driver.find_elements(By.XPATH,'//div[@class="Box"]/div/article/div[2]/a[1]')
    for i in counts_tags:
        count=i.text
        counts.append(count)



    languages_tags=driver.find_elements(By.XPATH,'//div[@class="Box"]/div/article/div[2]/span[1]')
    for i in languages_tags:
        language=i.text
        languages.append(language)
        
except Exception as e:
    print("error:",str(e))

Q.5-Scrape the details of top 100 songs on billiboard.com. Url = https:/www.billboard.com/ You have to find the
following details: 
# In[273]:


driver=webdriver.Chrome()
driver.get("https://www.billboard.com/")


# In[274]:


designation1=driver.find_element(By.XPATH,'/html/body/div[3]/header/div/div[2]/div/div/div[2]/div[2]/div/div/nav/ul/li[1]/a')
designation1.click()


# In[276]:


designation1=driver.find_element(By.XPATH,'/html/body/div[3]/main/div[2]/div[1]/div[1]/div/div/div[3]/a')
designation1.click()


# In[277]:


Songs=[]
Artists=[]
LWRs=[]
Peakranks=[]
Weeks=[]


# In[278]:


try:
    Songs_tags=driver.find_elements(By.XPATH,'//div[@class="o-chart-results-list-row-container"]/ul/li[4]/ul/li[1]/h3')
    for i in Songs_tags:
        Song=i.text
        Songs.append(Song)

    Artists_tags=driver.find_elements(By.XPATH,'//div[@class="o-chart-results-list-row-container"]/ul/li[4]/ul/li[1]/span')
    for i in Artists_tags:
        Artist=i.text
        Artists.append(Artist)


    LWRs_tags=driver.find_elements(By.XPATH,'//div[@class="o-chart-results-list-row-container"]/ul/li[4]/ul/li[4]')
    for i in LWRs_tags:
        LWR=i.text
        LWRs.append(LWR)


    Peakranks_tags=driver.find_elements(By.XPATH,'//div[@class="o-chart-results-list-row-container"]/ul/li[4]/ul/li[5]')
    for i in Peakranks_tags:
        Peakrank=i.text
        Peakranks.append(Peakrank)


    Weeks_tags=driver.find_elements(By.XPATH,'//div[@class="o-chart-results-list-row-container"]/ul/li[4]/ul/li[6]')
    for i in Weeks_tags:
        Week=i.text
        Weeks.append(Week)
        
except Exception as e:
    print("error:",str(e))


# In[279]:


import pandas as pd
pd.DataFrame({'Songs':Songs,'Artists':Artists,'Last week rank':LWRs,'Peak ranks':Peakranks,'Weeks on board':Weeks
})

Question.6-Scrape the details of Highest selling novels. 
# In[281]:


driver=webdriver.Chrome()
driver.get("https://www.theguardian.com/news/datablog/2012/aug/09/best-selling-books-all-time-fifty-shades-grey-compare")


# In[282]:


Books=[]
Authors=[]
Volumes=[]
Publishers=[]
Genres=[] 


# In[284]:


try:
    Books_tags=driver.find_elements(By.XPATH,'//table[@class="in-article sortable"]/tbody/tr/td[2]')
    for i in Books_tags:
        Book=i.text
        Books.append(Book)

    Authors_tags=driver.find_elements(By.XPATH,'//table[@class="in-article sortable"]/tbody/tr/td[3]')
    for i in Authors_tags:
        Author=i.text
        Authors.append(Author)


    Volumes_tags=driver.find_elements(By.XPATH,'//table[@class="in-article sortable"]/tbody/tr/td[4]')
    for i in Volumes_tags:
        Volume=i.text
        Volumes.append(Volume)


    Publishers_tags=driver.find_elements(By.XPATH,'//table[@class="in-article sortable"]/tbody/tr/td[5]')
    for i in Publishers_tags:
        Publisher=i.text
        Publishers.append(Publisher)


    Genres_tags=driver.find_elements(By.XPATH,'//table[@class="in-article sortable"]/tbody/tr/td[6]')
    for i in Genres_tags:
        Genre=i.text
        Genres.append(Genre)
        
except Exception as e:
    print("error:",str(e))


# In[285]:


import pandas as pd
pd.DataFrame({'Book':Books,'Author':Authors,'Volume':Volumes,'Publisher':Publishers,'Genre':Genres
})

Question7-Scrape the details most watched tv series of all time from imdb.com.
Url = https://www.imdb.com/list/ls095964455/ 
# In[228]:


driver=webdriver.Chrome()
driver.get("https://www.imdb.com/search/title/?title_type=tv_series&sort=num_votes,desc")


# In[229]:


Names=[]
Years=[]
Genres=[]
Runtimes=[]
Ratings=[]
Votes=[] 


# In[230]:


try:
    Names_tags=driver.find_elements(By.XPATH,'//div[@class="ipc-title ipc-title--base ipc-title--title ipc-title-link-no-icon ipc-title--on-textPrimary sc-be6f1408-9 srahg dli-title"]')
    for i in Names_tags:
        Name=i.text
        Names.append(Name)

    Years_tags=driver.find_elements(By.XPATH,'//DIV[@class="sc-be6f1408-7 iUtHEN dli-title-metadata"]/span[1]')
    for i in Years_tags:
        Year=i.text
        Years.append(Year)


    Genres_tags=driver.find_elements(By.XPATH,'//span[@class="sc-be6f1408-1 dbnleL"]/span')
    for i in Genres_tags:
        Genre=i.text
        Genres.append(Genre)


    Runtime_tags=driver.find_elements(By.XPATH,'//div[@class="sc-be6f1408-7 iUtHEN dli-title-metadata"]/span[2]')
    for i in Runtime_tags:
        Runtime=i.text
        Runtimes.append(Runtime)


    Ratings_tags=driver.find_elements(By.XPATH,'//div[@class="sc-e2dbc1a3-0 ajrIH sc-be6f1408-2 dAeZAQ dli-ratings-container"]/span')
    for i in Ratings_tags:
        Rating=i.text
        Ratings.append(Rating)

    Votes_tags=driver.find_elements(By.XPATH,'//div[@class="sc-f24f1c5c-0 cPpOqU"]')
    for i in Votes_tags:
        Vote=i.text
        Votes.append(Vote)
        
except Exception as e:
    print("error:",str(e))


# In[231]:


import pandas as pd
pd.DataFrame({'Names':Names,'Years':Years,'Genres':Genres,'Runtimes':Runtimes,'Ratings':Ratings,'Votes':Votes
})

Question.8-Details of Datasets from UCI machine learning repositories.
Url = https://archive.ics.uci.edu/ 
# In[164]:


driver=webdriver.Chrome()
driver.get("https://archive.ics.uci.edu/")


# In[165]:


designation1=driver.find_element(By.XPATH,'/html/body/div/div[1]/div[1]/main/div/div[1]/div/div/div/a[1]')
designation1.click()


# In[168]:


Datasets=[]
Datatypes=[]
Tasks=[]
Attributes=[]
instances=[]
Numbers=[]


# In[169]:


try:
    Datasets_tags=driver.find_elements(By.XPATH,'//div[@class="relative col-span-8 sm:col-span-7"]/h2')
    for i in Datasets_tags:
        Dataset=i.text
        Datasets.append(Dataset)

    Datatypes_tags=driver.find_elements(By.XPATH,'//div[@class="relative col-span-8 sm:col-span-7"]/p')
    for i in Datatypes_tags:
        Datatype=i.text
        Datatypes.append(Datatype)


    Tasks_tags=driver.find_elements(By.XPATH,'//div[@class="my-2 hidden gap-4 md:grid grid-cols-12"]/div[1]')
    for i in Tasks_tags:
        Task=i.text
        Tasks.append(Task)


    Attributes_tags=driver.find_elements(By.XPATH,'//div[@class="my-2 hidden gap-4 md:grid grid-cols-12"]/div[2]')
    for i in Attributes_tags:
        Attribute=i.text
        Attributes.append(Attribute)


    instances_tags=driver.find_elements(By.XPATH,'//div[@class="my-2 hidden gap-4 md:grid grid-cols-12"]/div[3]')
    for i in instances_tags:
        instance=i.text
        instances.append(instance)

    Numbers_tags=driver.find_elements(By.XPATH,'//div[@class="my-2 hidden gap-4 md:grid grid-cols-12"]/div[4]')
    for i in Numbers_tags:
        Number=i.text
        Numbers.append(Number)
        
except Exception as e:
    print("error:",str(e))


# In[171]:


import pandas as pd
pd.DataFrame({'Datasets':Datasets,'Datatypes':Attributes,'Tasks':Tasks,'instances':instances,'Numbers':Numbers
})


# In[ ]:




