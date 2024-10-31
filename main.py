import requests
import json
import csv

github_api_url = 'https://api.github.com/search/users'
url_for_details_about_user = 'https://api.github.com/users/{}'
users_repo_url = 'https://api.github.com/users/{}/repos'
name_url = 'https://api.github.com/users/{}'

headers = {
    'Authorization':''
}

def get_mumbai_users():
    query = 'location:Mumbai followers:>50'
    response = requests.get(github_api_url,params={'q':query},headers=headers)

    if response.status_code == 200:
        return response.json()['items']
    else:
        print(f'Error Fetching users:{response.status_code}')
        return 

def get_user_repo(username):
    response = requests.get(users_repo_url.format(username),headers=headers)

    if response.status_code == 200:
        return response.json()
    elif response.status_code == 404:
        print("Not found")
    else:
        print(f'Error Fetching repos:{response.status_code}')
        return 

def write_users_csv(users):
    with open('users.csv','w',newline='',encoding='utf-8') as f:
        writer = csv.DictWriter(f, fieldnames=[
            'login', 'name','company','location','email','hireable','bio',
        'public_repos','followers','following','created_at'
        ])
        writer.writeheader()
        for user in users:
            user_name = user['login']
            res = requests.get(url_for_details_about_user.format(user_name),headers=headers).json()
            print(res)

            user_data = {
                "login":res['login'],
                'name': user_name,
                'company':res['company'],
                'location':res['location'],
                'email':res['email'],
                'hireable':res['hireable'],
                'bio':res['bio'],
                'public_repos':res['public_repos'],
                'followers':res['followers'],
                'following':res['following'],
                'created_at':res['created_at']
            }
            writer.writerow(user_data)
def write_repos_csv(user,repos):
    with open('repositories.csv','a',newline='',encoding='utf-8') as f:
        fieldnames = [
            'owner["login"]','full_name','created_at','stargazers_count','watchers_count',
            'language','has_projects','has_wiki','license_name'
        ]
        writer = csv.DictWriter(f,fieldnames=fieldnames)
        writer.writeheader()
        for repo in repos:
            repo_data = {
                "owner_login":repo['owner']["login"],
                'full_name':repo['full_name'],
                'created_at':repo['created_at'],
                'stargazers_count':repo['stargazers_count'],
                'watchers_count':repo['watchers_count'],
                'language':repo['language'],
                'has_projects':repo['has_projects'],
                'has_wiki':repo['has_wiki'],
                'license_name':repo['license']['key'] if repo['license'] else None

            }
            writer.writerow(repo_data)


def main():
    users = get_mumbai_users()
    write_users_csv(users)

    for user in users:
        repos = get_user_repo(user['login'])
        write_repos_csv(user,repos)

if __name__ == '__main__':
    main()