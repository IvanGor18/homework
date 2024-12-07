import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('/home/goblin/Desktop/Informatics/homework/Mall_Customers.csv', sep=',')

income_for_genre = df.groupby("Genre")["Annual Income (k$)"].mean()

print(f"median female income  {(income_for_genre["Female"])} k($)")
###3
max_spending_by_genre = df.groupby("Genre")["Spending Score (1-100)"].max()

print(max_spending_by_genre)
####4
male = df[df["Genre"] == "Male"]
female = df[df["Genre"] == "Female"]
male = male.set_index("Age")
male = male.sort_values(by=["Age"])

#plot =male["Annual Income (k$)"].plot(ylabel="Annual Income (k$)")

# plt.scatter(male, male["Annual Income (k$)"])
spending_by_genre = df.groupby("Genre")["Spending Score (1-100)"].mean()
rate_for_genre = income_for_genre/spending_by_genre

print(rate_for_genre, type(rate_for_genre))

print(rate_for_genre['Female'])
print(rate_for_genre["Male"])
plt.bar('Female', rate_for_genre['Female'], width=1, color='pink', label='Значения 1')
plt.bar('Male', rate_for_genre["Male"], width=1, color='blue', label='Значения 2')
plt.show()
