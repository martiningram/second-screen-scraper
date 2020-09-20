# Second Screen Scraper

This utility scrapes data from ATP & InfoSys' "Second Screen" project. This
includes shot speeds, spin rates, as well as serve and return locations, among
many other things.

## Requirements

* Python 3
* beautifulsoup4 (for scraping)
* tqdm (for progress bars)

## Usage

The script `scrape_all.py` can be run as follows:

```
python scrape_all.py YEAR
```

It will then go through the tournaments for the given year and save the results
in JSON format to `./results`. If all goes well, that folder should then contain
three subfolders:

1. `results/match_info`: This contains JSON files with general match
   information, such as tournament name
2. `results/second_screen`: This contains "Second Screen" data, such as the
   serve locations.
3. `results/widget_data`: This contains data used for the widget on the Second
   Screen page, which includes stats like average shot speeds.
   
Each JSON file is identified by a string name consisting of
`YEAR_TOURNAMENT_MATCH`.

