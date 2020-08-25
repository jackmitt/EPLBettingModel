import pandas as pd
import numpy as np
from miscFcns import standardizeTeamName

league = input("1 for EPL, 2 for Serie A: ")
if (int(league) == 1):
    df = pd.read_csv('./EPL_Csvs/understatGameStats.csv', encoding = "ISO-8859-1")
    df2 = pd.read_csv('./EPL_Csvs/EPLHistoricOdds.csv', encoding = "ISO-8859-1")
    df3 = pd.read_csv('./EPL_Csvs/whoscoredGameStats.csv', encoding = "ISO-8859-1")
elif (int(league) == 2):
    df = pd.read_csv('./SerieA_Csvs/understatGameStats.csv', encoding = "ISO-8859-1")
    df2 = pd.read_csv('./SerieA_Csvs/whoscoredGameStats.csv', encoding = "ISO-8859-1")
    df3 = pd.read_csv('./SerieA_Csvs/1x2.csv', encoding = "ISO-8859-1")
    df4 = pd.read_csv('./SerieA_Csvs/ah.csv', encoding = "ISO-8859-1")
    df5 = pd.read_csv('./SerieA_Csvs/ou.csv', encoding = "ISO-8859-1")
    print (len(df.index), len(df2.index), len(df3.index), len(df4.index), len(df5.index))
    df = df.drop_duplicates(ignore_index = True)
    df2 = df2.drop_duplicates(ignore_index = True)
    df3 = df3.drop_duplicates(ignore_index = True)
    df4 = df4.drop_duplicates(ignore_index = True)
    df5 = df5.drop_duplicates(ignore_index = True)
    print (len(df.index), len(df2.index), len(df3.index), len(df4.index), len(df5.index))
    df.to_csv("./SerieA_Csvs/understatGameStats.csv")
    df2.to_csv("./SerieA_Csvs/whoscoredGameStats.csv")
    df3.to_csv("./SerieA_Csvs/1x2.csv")
    df4.to_csv("./SerieA_Csvs/ah.csv")
    df5.to_csv("./SerieA_Csvs/ou.csv")
else:
    print ("bad input")
