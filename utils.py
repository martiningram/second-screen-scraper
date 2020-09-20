import requests
from bs4 import BeautifulSoup


def get_tournament_result_links(year):

    page = requests.get(
        f'https://www.atptour.com/en/scores/results-archive?year={year}')

    soup = BeautifulSoup(page.content, 'html.parser')

    all_results = soup.find_all('tr', attrs={'class': 'tourney-result'})

    # This is a bit tenuous as it relies on the class of the a element...
    all_result_links = [x.find('a', attrs={'class':
                                           'button-border'}).get('href') for x
                        in all_results]

    to_add = 'https://www.atptour.com'

    with_prefix = [to_add + x for x in all_result_links]

    return with_prefix


def get_second_screen_ids(tournament_result_link):

    page = requests.get(tournament_result_link)

    soup = BeautifulSoup(page.content, 'html.parser')

    all_buttons = soup.find_all('a', attrs={'class': 'button-border'})

    all_links = [x.get('href') for x in all_buttons]
    second_screen = [x for x in all_links if 'second-screen' in x]

    split_second_screen = [x.split('/') for x in second_screen]

    info = [{'year': x[-3], 'tour_id': x[-2], 'match_id': x[-1]}
            for x in split_second_screen]

    return info


def fetch_second_screen_json(year, tour_id, match_id):

    url = (f'https://www.atptour.com/-/ajax/HawkEyeSecondScreen/'
           f'{year}/{tour_id}/{match_id}/')

    r = requests.get(url)

    return r.json()


def fetch_match_info_json(year, tour_id, match_id):

    url = (f'https://www.atptour.com/-/ajax/HawkEyeSecondScreen/MatchStats/'
           f'en/False/{year}/{tour_id}/{match_id}')

    r = requests.get(url)

    return r.json()


def fetch_widget_info_json(year, tour_id, match_id):
    # Includes spin etc.

    url = (f'https://www.atptour.com/-/ajax/HawkEyeSecondScreen/'
           f'{year}/{tour_id}/{match_id}/widget')

    r = requests.get(url)

    return r.json()
