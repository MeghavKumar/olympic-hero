# --------------
#Importing header files
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#Path of the file
path
data = pd.read_csv(path)

#Code starts here
data.rename(columns = {'Total' :'Total_Medals'},inplace = True)
print(data.head(10))



# --------------
#Code starts here





data['Better_Event']= np.where(data['Total_Summer']>data['Total_Winter'],'Summer',
(np.where(data['Total_Summer']<data['Total_Winter'],'Winter','Both')))
#print(data['Better_Event'])
summ_med= data['Better_Event'].value_counts()
print(summ_med)
#wint_med=data['Winter'].value_counts()
if summ_med[0]>summ_med[1]:
    better_event = 'Summer'
elif summ_med[0]<summ_med[1]:
    better_event = 'Winter'
else:
    better_event = 'Both'
print(better_event)





#print(wint_med)
#better_event = np.where(summ_med>wint_med,'Summer','Winter')
#data['Better_Event'].value.counts()
print(better_event)





# --------------
#Code starts here




top_countries = data[['Country_Name','Total_Summer', 'Total_Winter','Total_Medals']].copy()

top_countries.drop(top_countries.tail(1).index, inplace = True)

def top_ten(top_countries , top):
    country_list = []
    country_list=top_countries.nlargest(10,top)
    return country_list

top_10_s = top_ten(top_countries,'Total_Summer')
top_10_summer =[]
top_10_summer = top_10_s['Country_Name'].tolist()
top_10_win = top_ten(top_countries,'Total_Winter')
top_10_winter =[]
top_10_winter = top_10_win['Country_Name'].tolist()
top_tan = top_ten(top_countries,'Total_Medals')
top_10 =[]
top_10 = top_tan['Country_Name'].tolist()

print(top_10_summer)
print(top_10_winter)
print(top_10)
com= set(top_10_summer).intersection(top_10_winter, top_10)
common=list(com)
print(common)
    


# --------------
#Code starts here

summer_df = data[data['Country_Name'].isin(top_10_summer)]
print(summer_df)
winter_df = data[data['Country_Name'].isin(top_10_winter)]
print(winter_df)
top_df = data[data['Country_Name'].isin(top_10)]
print(top_df)
plt.bar(summer_df['Country_Name'],summer_df['Total_Summer'])
plt.show()
plt.bar(winter_df['Country_Name'],winter_df['Total_Summer'],color = 'g')
plt.show()
plt.bar(top_df['Country_Name'],top_df['Total_Summer'],color = 'r')
plt.show()


# --------------
#Code starts here
# Summer Ratio
summer_df['Golden_Ratio'] = summer_df['Gold_Summer']/summer_df['Total_Summer']

sort_by = summer_df.sort_values('Golden_Ratio',ascending=False)
summer_max_ratio = sort_by['Golden_Ratio'].iloc[0]
print(summer_max_ratio)
summer_country_gold = sort_by['Country_Name'].iloc[0]
print(summer_country_gold)

# Winter Ratio

winter_df['Golden_Ratio'] = winter_df['Gold_Winter']/winter_df['Total_Winter']

sort_by_1 = winter_df.sort_values('Golden_Ratio',ascending=False)
winter_max_ratio = sort_by_1['Golden_Ratio'].iloc[0]
print(winter_max_ratio)
winter_country_gold = sort_by_1['Country_Name'].iloc[0]
print(winter_country_gold)


# Total Top Ratio

top_df['Golden_Ratio'] = top_df['Gold_Total']/top_df['Total_Medals']

sort_by_2 = top_df.sort_values('Golden_Ratio',ascending=False)
top_max_ratio = sort_by_2['Golden_Ratio'].iloc[0]
print(top_max_ratio)
top_country_gold= sort_by_2['Country_Name'].iloc[0]
print(top_country_gold)


# --------------
#Code starts here

#data_1 = data.copy()
#data_1=data_1.drop(data_1.tail(1).index, inplace = True)
#print(data_1.head(1))

data_1  = data.iloc[:-1]

#GT =data_1['Gold_Total'].value_counts()
#print(GT)
#GTT =GT*3
#print(GTT)
data_1['Total_Points'] = data_1.loc[:,'Gold_Total'].mul(3)+data_1.loc[:,'Silver_Total'].mul(2)+data_1.loc[:,'Bronze_Total'].mul(1)

sort_by5 = data_1.sort_values('Total_Points',ascending=False)
most_points = sort_by5['Total_Points'].iloc[0]
print(most_points)

best_country = sort_by5['Country_Name'].iloc[0]
print(best_country)



# --------------
#Code starts here

best = data[data['Country_Name'] == best_country]
sd = best[['Gold_Total','Silver_Total','Bronze_Total']]
best = sd
best.plot.bar()
plt.xlabel("United States")
plt.ylabel("Medals Tally")
plt.xticks(rotation =45)
plt.show()


