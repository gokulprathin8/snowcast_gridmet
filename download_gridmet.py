import os
import requests
from bs4 import BeautifulSoup
from utils import download_files

if not os.path.exists('grid-met'):
    os.makedirs('grid-met')
download_links = list()
base_url = "https://www.northwestknowledge.net/metdata/data/"

r = requests.get("https://www.northwestknowledge.net/metdata/data/")
soup = BeautifulSoup(r.content, "html.parser")
href_links = soup.find_all("a", href=True)
for h in href_links:
    if any(substring in h['href'] for substring in ['bi_', 'pet_', 'pr_', 'rmin_', 'rmax_', 'tmmn_', 'tmmx_', 'vpd_', 'vs_']) and not h['href'].startswith('eddi'):
        download_links.append(base_url + h['href'])

print(download_links)
download_files(download_links, output_dir="./grid-met")
