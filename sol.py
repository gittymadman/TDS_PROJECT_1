import pandas as pd
import numpy as np
from scipy.stats import linregress
from datetime import datetime
users = pd.read_csv('users.csv')
repo = pd.read_csv('repositories.csv')

# ans_1 = users.sort_values(by='created_at',ascending=[True])
# print(ans_1.head())

# Next
# filtered_users = repo.dropna(subset=['license_name'],axis=0)

# top_3 = filtered_users.groupby('license_name').size().sort_values(ascending=False).index.tolist()

# top_license_str = ','.join(top_3)
# print(top_license_str)

# Next

# company = users.dropna(subset=['company'],axis=0)

# top_3 = company.groupby('company').size().sort_values(ascending=False).index.tolist()
# print(top_3)


# lang = repo.dropna(subset=['language'],axis=0)
# lang = lang[]
# top_3 = lang.groupby('language').size().sort_values(ascending=False)
# print(top_3)

# new_df = pd.merge(users,repo,on='login')
# print(new_df.groupby('language').size().sort_values(ascending=False))
# new_df = new_df[new_df['created_at_x']>='2020-01-01']
# print(new_df.groupby('language').size().sort_values(ascending=False))

# stars = repo[['language','stargazers_count']]
# print(stars.groupby('language')['stargazers_count'].mean().sort_values(ascending=False))

# strength = users[['login','followers','following']]
# strength['leader_strength'] = strength['followers']/(1+strength['following'])
# strength = strength.sort_values('leader_strength',ascending=False)
# print(strength)

# repo['has_wiki'] = np.where(repo['has_wiki'],1,0)
# x = repo['has_wiki']
# y = repo['has_projects']
# print(x.corr(y))
# slope, intercept, r_score, p_value,std_err = linregress(y,x)
# print(slope)

# mean_for_hireable = users[users['hireable']==True]

# mean_for_not_hireable = users[users['hireable']==False]
# mean_for_hireable = mean_for_hireable['following'].mean()
# mean_for_not_hireable = mean_for_not_hireable['following'].mean()
# print(mean_for_hireable - mean_for_not_hireable)

# bio = users['bio'].str.split().str.len()>0
# filtered_based_bio = users[bio].copy()
# filtered_based_bio.loc[:,'length_bio'] = filtered_based_bio['bio'].str.len() 
# x = filtered_based_bio['length_bio']
# y = filtered_based_bio['followers']
# slope,itercept,r_score,p_value,std_err = linregress(x,y)
# print(slope) NOT Working

# def week(date):
#     date = date.split('T')[0]
#     date_obj = datetime.strptime(date,"%Y-%m-%d")
    
#     if date_obj.weekday() > 5:
#         return "Weekend"
#     else:
#         return "Weekday"

# repo['Day_of_week'] = repo["created_at"].apply(week)

# weekend_repos = repo[(repo['Day_of_week']=='Weekend')]  
# print(repo)
# print(weekend_repos.groupby('login').size().sort_values(ascending=False).head(5))\

def sur(name):
    name = str(name).split()[-1]
    return name

sur_user_df = users['name'].dropna().apply(sur).value_counts()
print(sur_user_df)



