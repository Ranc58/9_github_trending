import requests
import datetime


def get_repositories_json():
    todays_date = datetime.date.today()
    search_period = 7
    date_period = datetime.timedelta(days=search_period)
    date_interval_for_search = 'created:>=' + str(todays_date - date_period)
    repo_sort_type = 'stars'
    repos_output = '20'
    search_params = {'q': date_interval_for_search,
                     'sort': repo_sort_type,
                     'per_page': repos_output}
    return_repos = requests.get('https://api.github.com/search/repositories',
                                params=search_params)
    trended_new_repos_json = return_repos.json()['items']
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
