def atmosphin(file,first_date,last_date):#example first date='1995-12-06'
    import numpy as np
    import pandas as pd
    date1=pd.date_range(first_date, last_date)
    with open(file) as f:
        contents = f.readlines()[7:-1]
        df=pd.DataFrame(columns=['tAtm','Prec','rSoil','rRoot','hCritA','rt','ht','rt','ht','rt','ht','rt','ht']) # Create a Dic for creating DF later
    day=[]
    Rain=[]
    Ep=[]
    Tp=[]

    for i in range(np.size(contents)):
        aa=contents[i][:-1].split(",")#this takes every row       
        y=((aa[0]).split(" "))
        aa=[e for e in y if e]
        day.append(float(aa[0]))
        Rain.append(float(aa[1]))
        Ep.append(float(aa[2]))
        Tp.append(float(aa[3]))
    df = pd.DataFrame({'day':day,'Rain':Rain,'Ep':Ep,'Tp':Tp})
    df["Date"]=date1
    df["month"]=pd.DatetimeIndex(df['Date']).month
    df["year"]=pd.DatetimeIndex(df['Date']).year
    atmosph=df
    return atmosph

        
