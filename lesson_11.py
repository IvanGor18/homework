# 1
import pandas as pd
import numpy as np
import scipy.stats as stats

df = pd.read_csv('NISPUF17.csv', sep=',')

def proportion_of_education(dataframe):

    len_of_df = len(df)

    less_12 = round(float(df['EDUC1'].where(df['EDUC1'] == 1).count() / len_of_df), 2)
    eq_12 = round(float(df['EDUC1'].where(df['EDUC1'] == 2).count() / len_of_df), 2)
    more_12 = round(float(df['EDUC1'].where(df['EDUC1'] == 3).count() / len_of_df), 2)
    college  = round(float(df['EDUC1'].where(df['EDUC1'] == 4).count() / len_of_df), 2)

    prop_of_educ = {
                    "less than 12": less_12,
                    "12": eq_12,
                    "more than 12": more_12,
                    "college": college
                    }
    
    print(prop_of_educ)

# 2

def average_influenza_doses(dataframe):
    
    bm_y = df.groupby('CBF_01')['P_NUMFLU'].mean()
    bm_tuple = (round(float(bm_y[1]), 1), round(float(bm_y[2]), 1))

    print(bm_tuple)


# 3

def chickenpox_by_sex(dataframe):

    maleDf = df[df["SEX"] ==1]
    femaleDf = df[df["SEX"] == 2]

    doses1 = maleDf[maleDf["P_NUMVRC"] >= 1]
    doses2 = femaleDf[femaleDf["P_NUMVRC"] >= 1]

    chichkenPox1_1 = doses1[doses1["HAD_CPOX"] == 1]
    chichkenPox1_2 = doses1[doses1["HAD_CPOX"] == 2]

    count1_1 = chichkenPox1_1["SEX"].count()
    count1_2 = chichkenPox1_2["SEX"].count()

    chichkenPox2_1 = doses2[doses2["HAD_CPOX"] == 1]
    chichkenPox2_2 = doses2[doses2["HAD_CPOX"] == 2]

    count2_1 = chichkenPox2_1["SEX"].count()
    count2_2 = chichkenPox2_2["SEX"].count()

    resultMale = count1_1/count1_2
    resultFemale = count2_1/count2_2
    
    result = {
            "male": float(round(resultMale,4)),
            "female": float(round(resultFemale,4))
              }

    print(result)

proportion_of_education(df)
average_influenza_doses(df)
chickenpox_by_sex(df)