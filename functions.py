#!/usr/bin/env python
# -*- coding: utf-8 -*-

import numpy as np
import pandas as pd

import matplotlib.pyplot as plt
import seaborn as sns

def valores_ds1(df):
    """ Toma sólo las columnas categóricas de un df y cuenta cuantos valores diferentes tiene cada columna (incluye NaN9) Requiere el parámetro df. """
    for i in df.select_dtypes(exclude=[np.number]).columns.tolist():
        print(i,':')
        print(df[i].value_counts(dropna=False))
        print('\n')


def valores_ds1_grouped(df):
    """ Toma sólo las columnas no numéricas de un df y cuenta cuantos valores únicos tienen, agrupados por region. """
    df2=df.groupby('region')
    for i in df.select_dtypes(exclude=np.number).columns.tolist():
        if i != 'region':
            print(i,':')
            print(df2[i].value_counts(dropna=False, normalize=True))
            print('\n')
            

def histograms(df):
    """ Selecciona las columnas numéricas de un dataframe (df) y grafica el histograma de cada columna. """
    for i in df.select_dtypes(include=np.number).columns.tolist():
        plt.figure()
        plt.hist(df[i])
        plt.title(i)
        plt.axvline(df[i].mean(), color='tomato', linestyle='--', lw=2)


def boxplots(df):
    """ Selecciona las columnas numéricas de un dataframe (df) y grafica el box plot de cada columna. """
    sns.set(style="whitegrid")
    for i in df.select_dtypes(include=[np.number]).columns.tolist():
        plt.figure()
        sns.boxplot(df[i])
        plt.title(i)
        
def histograms_bins(df):
    """ Selecciona las columnas numéricas de un dataframe (df) y grafica el histograma de cada columna. Además, ajusta el tamaño de los bins, ya que la heurística para seleccionar el tamaño no funciona bien en variables enteras """
    for i in df.select_dtypes(include=np.number).columns.tolist():
        plt.figure()
        sns.distplot(df[i], bins= np.count_nonzero(df[i].unique()), kde=False)
        plt.title(i)
        plt.axvline(df[i].mean(), color='tomato', linestyle='--', lw=2)