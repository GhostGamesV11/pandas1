import numpy as np
import pandas as pd
import xlrd
import openpyxl

#zad1
imiona=pd.ExcelFile("imiona.xlsx")
df=pd.read_excel(imiona, header=0)
print(df)

#zad2

print(df[df["Liczba"]>1000])
print("\n")
print(df.loc[df["Imie"]=="BARTOSZ"])
print("\n")
print(df["Liczba"].sum())
print("\n")
print(df.loc[(df["Rok"]<=2005)&(df["Rok"]>=2000),"Liczba"].sum())
print("\n")
print("Chlopcy =",df.loc[df["Plec"]=="M","Liczba"].sum())
print("Dziewczyny =",df.loc[df["Plec"]=="K","Liczba"].sum())
print("\n")
ch=df.loc[df["Plec"] == "M"]
sumach=ch.loc[ch.groupby("Rok")["Liczba"].idxmax()]
dzw=df.loc[df["Plec"]=="K"]
sumadzw=dzw.loc[dzw.groupby("Rok")["Liczba"].idxmax()]
chidzw=pd.concat([sumach, sumadzw])
print(chidzw.sort_values(by="Rok"))


#zad 3
df=pd.read_csv("zamowienia.csv",header=0,sep=";",decimal=".")
df["Data zamowienia"]=pd.to_datetime(df["Data zamowienia"])
print(df["Sprzedawca"].unique())
print("\n")
print(df.sort_values(by=["Utarg"],ascending=False).head(5))
print("\n")
print(df.groupby("Sprzedawca")["idZamowienia"].nunique())
print("\n")
print(df.groupby("Kraj")["idZamowienia"].nunique())
print("\n")
suma= df.loc[(df["Kraj"]=="Polska")&(df["Data zamowienia"].dt.year==2004)]
print(suma["idZamowienia"].nunique())


