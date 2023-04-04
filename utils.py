import os
import requests
import threading


def download_file(url, filepath):
    try:
        response = requests.get(url)
        with open(filepath, "wb") as f:
            f.write(response.content)
    except:
        print(f"Could not download file with url: {url}")


def download_files(urls, output_dir):
    threads = []
    for url in urls:
        filename = os.path.basename(url)
        filepath = os.path.join(output_dir, filename)
        t = threading.Thread(target=download_file, args=(url, filepath))
        threads.append(t)
        t.start()
    for t in threads:
        t.join()
