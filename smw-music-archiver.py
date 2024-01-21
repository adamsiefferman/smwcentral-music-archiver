import requests
from bs4 import BeautifulSoup
import time
import os
import urllib.parse

''' working python script to download all the files from the smw music section of smwcentral.net
    pagination is a little funky due to the way the site is set up, so the total_pages variable needs to be updated manually if the number of pages changes
    this script is a little slow due to the time.sleep() functions, but it's better than getting banned from the site for spamming requests
    the script will skip files that already exist in the directory, so you can run it multiple times without worrying about redownloading files
    the script will also skip files that are not .zip files, so you don't have to worry about downloading unwanted files
    this script is not intended for actual use since to scrape the entier music section of smwcentral.net
    i am not sure what their policy on bulk downloads is, so use this script at your own risk
    ultimately, this script is just a proof of concept for using beautifulsoup to scrape a website and come with no warranty or guarantee of functionality or safety of use '''

total_pages = 162  # Set the total number of pages (NOTE: THIS NEEDS TO BE UPDATED MANUALLY IF THE NUMBER OF PAGES CHANGES)
base_url = "https://www.smwcentral.net/?p=section&s=smwmusic&u=0&g=0&n="

def download_file(url, filename=None): #url is file url
    """Download a file from a URL"""
    if url.startswith("//"):
        url = "https:" + url

    if not filename:
        filename = url.split('/')[-1]

    # Send a GET request to the URL
    response = requests.get(url)

    # Check if the request was successful
    if response.status_code == 200:
        if os.path.exists(filename):
            print(f"File already exists, skipping {filename}")
        else:
            with open(filename, 'wb') as file:
                file.write(response.content)
                print(f"File downloaded: {filename}")
    else:
        print(f"Failed to download file: {filename}")

for page_num in range(1, total_pages + 1): #this section uses a for loop to paginate through all content pages 
    url = base_url + str(page_num) #concatenate the base url with the page number
    response = requests.get(url) 
    
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser') #parse the html content
        download_links = [] #empy list to store the download links
        table_content = soup.find('table', class_='list') #find the table with the class list
        for tr in table_content.find_all('tr'): #find all the tr tags in the table
            for td in tr.find_all('td'): #find all the td tags in the tr
                for link in td.find_all('a'): #find all the a tags in the td
                    if link.get('href').endswith('.zip'): #if the href ends with .zip
                        download_links.append(link.get('href')) #append the href to the download_links list
                    else: #if it doesn't end with .zip
                        continue #continue to the next link
        for current_link in download_links:
            download_file(urllib.parse.unquote(current_link)) #function call to download the file
            time.sleep(5) #respect that bandwidth yall
    else:
        print(f"Failed to retrieve page {page_num}")
    
    # Optionally, add a delay between requests to respect server load
    time.sleep(1)