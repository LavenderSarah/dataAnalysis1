import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


data = pd.read_excel('citybike.xlsx')

#Get the number of null values

print(data.isnull().sum())

#Fill it up

data.fillna('Not Specified', inplace=True)

#Check again for null values

print(data.isnull().sum())


#Q1: What are the most popular pick-up locations across the city for NY Citi Bike rental?

pickup = data['Start Station Name'].value_counts()

print(pickup)

mostrepspots = pickup.idxmax()

print("The most popular pickup spot is at:", mostrepspots)

fig, ax = plt.subplots(figsize=(10, 10))

sns.set(font_scale=1.0)

sns.countplot(y="Start Station Name", data=data,order=data['Start Station Name'].value_counts(ascending=True).index, palette="Set2")


#Q2: How does the average trip duration vary across different age groups?

averageduration_byage = data.groupby('Age Groups')['Trip_Duration_in_min'].mean().astype(int)

print(averageduration_byage)

plt.figure(figsize=(10, 6))
plt.bar(averageduration_byage.index, averageduration_byage)
plt.title("Average Trip Duration by Age Groups")
plt.xlabel("Age Groups")
plt.ylabel("Average Trip Duration (seconds)")
plt.xticks(rotation=45)
sns.barplot(x=data['Age Groups'], y=data['Trip Duration'], data=data, palette='pastel')
plt.show()


#Q3: Which age group rents the most bikes?

count = data.groupby('Age Groups').size()

print(count)
