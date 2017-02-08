# -*- coding: utf-8 -*-
"""
Created on Wed Jan 25 12:11:17 2017

@author: Kumari.Kirti
"""
df = pd.read_csv('C:\Users\Kumari.Kirti\Desktop\spr\data_duplicate\duplicates testing\keyword_clustering_samsung2.csv')
result = df[['Entity1_name','Entity2_name','Entity3_name','Entity5_name','Entity5_name']]
result=result[1:]
a=(result.values.tolist()) 
comb=[]   
for value in a:
   try: 
    b=(sorted((value),key = str.lower))
    comb.append("_".join(b)) 
   except: 
    c=(sorted(value))
    comb.append(c)
    continue

#for value in a:
#    b=sorted(value,key = str.lower)
#    comb.append("_".join(b)) 
se = pd.Series(comb)
df['comb'] = se.values