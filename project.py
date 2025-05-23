import pandas as pd
import matplotlib.pyplot as plt
df =pd.read_csv('ball_by_ball_it20.csv')
df.head()
df.drop(columns=['Unnamed: 0' , 'Ball Rebowled'],inplace=True)
df['Method'].fillna('Not out',inplace=True)
df['Player Out'].fillna('None',inplace=True)
df['Runs to Get'].fillna(0, inplace=True)
df['Player Out Runs'].fillna(0, inplace=True)
df['Player Out Balls Faced'].fillna(0,inplace=True)
print(df.isnull().sum())
df['Date']=pd.to_datetime(df['Date'] , errors='coerce', format=None)
df['Year']=df['Date'].dt.year
x = int(input("Most Runs by batter in Year"))
dfbatyear= df[df['Year']==x]
Run=dfbatyear.groupby('Batter')['Batter Runs'].sum().reset_index()
top10=Run.sort_values(by='Batter Runs', ascending=False).head(20)
print("Top 10 Batters with Highest Score :" )
print(top10[['Batter', 'Batter Runs']])
plt.figure(figsize=(10,6))
plt.bar(top10['Batter'],top10['Batter Runs'] , color=plt.cm.Paired.colors)
plt.xlabel('Batter')  # Label for x-axis
plt.ylabel('Runs')
plt.title('Top 20 Batters with Highest Runs in ' + str(x))
plt.xticks(rotation=20, ha='right')
plt.tight_layout()
plt.show()
y = int(input("Most Wickets by bowler in Year"))
dfbowlyear=df[df['Year']==y]
wickets=dfbowlyear.groupby('Bowler')['Wicket'].sum().reset_index()
top=wickets.sort_values(by='Wicket',ascending=False).head(20)
plt.figure(figsize=(10,6))
plt.bar(top['Bowler'],top['Wicket'] , color=plt.cm.Paired.colors)
plt.xlabel('Bowler') 
plt.ylabel('Wickets')
plt.title('Top 20 Bowlers with Highest Wickets in ' + str(y))
plt.xticks(rotation=20, ha='right')
plt.tight_layout()
plt.show()
print("Top 10 Bowlers with Highest wickets :" )
print(top[['Bowler', 'Wicket']])
score=df.groupby('Batter')['Batter Runs'].sum()
Dismissals = df[df['Player Out'] != 'None'].groupby('Batter').size()
avg_df = pd.DataFrame({'Total Score': score, 'Dismissals': Dismissals})
avg_df['Batting Average'] = avg_df['Total Score'] / avg_df['Dismissals']
avg_df = avg_df.reset_index()
avg_df = avg_df[avg_df['Dismissals'] >= 10]
avg = avg_df.sort_values(by='Batting Average', ascending=False).head(20)
print("Top 20 Batters with Highest Career Batting Averages")
print(avg[['Batter', 'Batting Average', 'Total Score', 'Dismissals']])
plt.figure(figsize=(10,6))
plt.bar(avg['Batter'],avg['Batting Average'] , color=plt.cm.Paired.colors)
plt.xlabel('Batter') 
plt.ylabel('Average')
plt.title('Top 20 Batter with Highest Average')
plt.xticks(rotation=20, ha='right')
plt.tight_layout()
plt.show()



