#This SPI program can predict the SPI for monthly time series subject to availability of rainfall data given input as csv file 

import pandas as pd
from sys import *
from math import *
from scipy import *
from scipy.integrate import quad
import numpy as np
from scipy.stats import gamma
from scipy.stats import norm
import matplotlib.pyplot as plt

df = pd.read_csv("https://raw.githubusercontent.com/bikash4044/CD61203/main/Rainfall_Kandhamal_monthly_(2).csv")
# df

time ="0123456789ab"
# def gamma(x):
#     pass

# def g(x):
#     v= (1/( (beta**alpha) * (gamma(alpha)) ))*(x**(alpha-1) * e**(-1*x/beta))
#     return v





def pltit(SPI,i):
  fig, bx = plt.subplots()
  bx.plot(year, SPI, label=r"$"+i+"$" )
  bx.legend();
  plt.savefig("/content/drive/MyDrive/CCWR/fig"+i+".png")

  # print(spi)
  # a = pd.DataFrame()
  # a["year"] = year
  # a["SPI"] = spi


def param(dat,label="temp"):
    global n, mean, A, alpha, beta, z, G, H
    zeros = 0
    for i in dat:
      if(i==0):
        zeros+=1
    z=0
    n=len(dat)
    s=0
    for i in range(n):
        s+=dat[i]
        if(dat[i]==0):
            z+=1
    mean=s/n

    slndat=0
    for i in range(n):
      if(dat[i]==0):
        pass
      else:
        slndat+=log(dat[i])

    A=log(mean)-(slndat/n)
    alpha = (0.25/A)*(1+sqrt(1+(4*A/3)))
    beta = mean / alpha
    # G=[]
    # H=[]
    # q=z/n
    # for i in range(n):
    #     Gx,err = quad(g,0,dat[i])
    #     G.append(Gx)
    #     h= q + (1-q)*Gx
    #     H.append(h)

    g = gamma.cdf(dat,a=alpha, scale=beta)
    global spi
    spi = norm.ppf(g, loc=0, scale=1)

    # pltit(spi,label)
    for i in range(len(dat)):
      if(dat[i]==0):
        spi[i]=1/zeros

    return spi


year = list(df["Rainfall"])
rf = list(df["Jun"])


param(rf,"spi")



def addt(n):
  for i in range(12-n+1):
    s=time[i:i+n]
    df4["temp"]=[0 for i in range(len(df4))]
    #sum to temp and store temp
    for j in s:
      df4["temp"]+=df4[j]
    df4[s]=df4["temp"]
#time searies dataframe
df3 = pd.DataFrame()
df4=df
df3["Years"]=df["Rainfall"]
df4=df4.drop(['Rainfall'], axis=1)
df4=df4.drop(['Total'], axis=1)
df4.columns = ['0','1','2','3','4','5','6','7','8','9','a','b']

#multi-time series
# t1=int(input("Enter no of time series:"))
# t2=[]
# for i in range(t1):
#   t2.append(int(input(f"Enter time series {i+1}:")))
#   if(t2[-1]>12 or t2[-1]<1):
#     print("invalid input!!!")
#     exit()
# #addt(2)


# for i in t2:
#   addt(i)

#singe time series
t=int(input(f"Enter time series:"))
addt(t)


df4=df4.drop(['temp'], axis=1)
df4


#df5 correponds to spi values for df4
df5=pd.DataFrame()
for col in df4.columns:
  df5[col]=param(df4[col])

df5


#table
dfx=pd.DataFrame()
for col in df5.columns:
  if(len(col)==t):
    dfx[col]=df5[col]

dfx


#plotting
# fig, ax = plt.subplots()

# for cols in df5.columns:
#   if(len(cols)==t):
#     ax.plot(year, df5[cols], label=cols)
# ax.legend();
