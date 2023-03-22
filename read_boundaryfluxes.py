def boundaryfluxes(file,first_date,last_date):#example first date='1995-12-06'
    import numpy as np
    import pandas as pd
    date1=pd.date_range(first_date, last_date)
    with open(file) as f:
        contents = f.readlines()[2:]
        df=pd.DataFrame(columns=['tAtm','Prec','rSoil','rRoot','hCritA','rt','ht','rt','ht','rt','ht','rt','ht']) # Create a Dic for creating DF later
    num=[]
    day=[]
    value=[]

    for i in range(np.size(contents)):
        aa=contents[i].split(",")#this takes every row       
        y=((aa[0]).split(" "))
        aa=[e for e in y if e]
        num.append(float(aa[0]))
        day.append(float(aa[1]))
        value.append(float(aa[2]))        
    df = pd.DataFrame({'num':num,'day':day,'value':value})
    df=df.drop_duplicates(['day'], keep='last')
    df=df.loc[df['day'].isin(range(np.shape(df)[0]))].reset_index()
    df["Date"]=date1
    df["month"]=pd.DatetimeIndex(df['Date']).month
    df["year"]=pd.DatetimeIndex(df['Date']).year
    flux=df
    return flux

        
