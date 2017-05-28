import requests
import json
import datetime


def get_repositories_json():
    todays_date = datetime.date.today()
    date_period = datetime.timedelta(days=7)
    date_interval_for_search = (todays_date - date_period)
    repo_sort_type = 'sort=stars'
    repos_quantity = 'per_page=20'
    api_return_repos = requests.get(
        'https://api.github.com/search/repositories?q=created:%3E={}&{}&{}'
        .format(date_interval_for_search, repo_sort_type, repos_quantity))
    trended_new_repos_json = api_return_repos.json()['items']
    return trended_new_repos_json


def print_most_trended_repos(trended_new_repos):
    for repo in trended_new_repos:
        print('\nRepository: {}\nlink: {}\nstars: {}\nopen issues: {}\n'.format
              (repo['name'],
               repo['html_url'],
               repo['stargazers_count'],
               repo['open_issues_count']))


if __name__ == '__main__':
    try:
        trended_new_repos = get_repositories_json()
    except requests.exceptions.ConnectionError:
        print('Failed! Check Your connection.')
    else:
        print_most_trended_repos(trended_new_repos)
