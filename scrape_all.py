import sys
from utils import (
    get_tournament_result_links, get_second_screen_ids, fetch_match_info_json,
    fetch_second_screen_json)
from tqdm import tqdm
from os import makedirs
from os.path import join, isfile
import json


year = sys.argv[1]

tournament_links = get_tournament_result_links(year)

target_dir = './results'

makedirs(target_dir, exist_ok=True)

match_info_dir = join(target_dir, 'match_info')
ss_dir = join(target_dir, 'second_screen')

failed_files = open(join(target_dir, 'failed.txt'), 'w')

makedirs(ss_dir, exist_ok=True)
makedirs(match_info_dir, exist_ok=True)

cache = True

for cur_link in tournament_links:

    print(cur_link)

    ss_ids = get_second_screen_ids(cur_link)

    if len(ss_ids) == 0:
        continue

    for cur_ss_id in tqdm(ss_ids):

        cur_identifier = '_'.join(cur_ss_id.values())

        match_info_file = join(match_info_dir, cur_identifier + '.json')
        ss_file = join(ss_dir, cur_identifier + '.json')

        if isfile(match_info_file) and isfile(ss_file) and cache:
            continue

        try:
            ss_json = fetch_second_screen_json(**cur_ss_id)
            match_json = fetch_match_info_json(**cur_ss_id)
        except json.JSONDecodeError:
            print(cur_identifier, file=failed_files)
            continue

        with open(match_info_file, 'w') as f:
            json.dump(match_json, f)

        with open(ss_file, 'w') as f:
            json.dump(ss_json, f)
