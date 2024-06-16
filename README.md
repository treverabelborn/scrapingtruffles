# Truffle Mushrooms Web Scraper
This is a web scraping project that uses Scrapy and Python to scrape a website for truffle products.

## Setup & Run Locally
Install scrapy (I use `pipx`):
```
pipx install scrapy
```
Create and source a virtual environment:
```
python3 -m venv .venv && source .venv/bin/activate
```
Run the spider with:
```
scrapy crawl sabatino
```