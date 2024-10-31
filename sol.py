import pandas as pd

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


lang = repo.dropna(subset=['language'],axis=0)
lang = lang[]
top_3 = lang.groupby('language').size().sort_values(ascending=False)
print(top_3)