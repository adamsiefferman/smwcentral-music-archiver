Working python script to download all the files from the smw music section of smwcentral.net
Pagination is a little funky due to the way the site is set up, so the total_pages variable needs to be updated manually if the number of pages changes
This script is a little slow due to the time.sleep() functions, but it's better than getting banned from the site for spamming requests
The script will skip files that already exist in the directory, so you can run it multiple times without worrying about redownloading files
The script will also skip files that are not .zip files, so you don't have to worry about downloading unwanted files
This script is not intended for actual use since to scrape the entier music section of smwcentral.net
I am not sure what their policy on bulk downloads is, so use this script at your own risk
Ultimately, this script is just a proof of concept for using beautifulsoup to scrape a website and come with no warranty or guarantee of functionality or safety of use
Feel free to modify and learn from this code, as that was the point of doing this exercise


Have a great day! 
