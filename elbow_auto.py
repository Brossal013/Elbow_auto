# -*- coding: utf-8 -*-
"""
Created on Mon Dec 19 00:44:45 2022

@author: mossando
"""
from sklearn.cluster import KMeans
import numpy as np


def criterio_f(dedo,lim = 0.45,lim1_2 = 0.08 ,lim2 = 0.05):
 
 d = [] # Distorsión
 
 # Cálculo de Distorsión en k = {1,2}
 k=1
 kmeans = KMeans(n_clusters = k)
 kmeans.fit(dedo)
 d.append(kmeans.inertia_)
 k += 1
 kmeans = KMeans(n_clusters = k).fit(dedo)
 d.append(kmeans.inertia_)
 
 while True:
     
   if k <= 4:# Criterio indice CVA
     if d[k-1]/d[k-2] < lim:
       k += 1
       kmeans = KMeans(n_clusters = k).fit(dedo)
       d.append(kmeans.inertia_)
       if d[k-1]/d[k-2] > lim + lim1_2:
         break
     else:
       k += 1
       kmeans = KMeans(n_clusters = k).fit(dedo)
       d.append(kmeans.inertia_)
       
   if k >4:# Criterio indice CPPI
     if np.diff(d)[k-2]/(d[1]-d[0])  < lim2:
       break
     k += 1
     kmeans = KMeans(n_clusters = k).fit(dedo)
     d.append(kmeans.inertia_)
 return(k - 1) 