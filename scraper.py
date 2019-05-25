#Python programme to retrieve data from a blog post

# import libraries
from urllib.request import urlopen
from bs4 import BeautifulSoup


# url of the site
quote_page = "https://se15053.blogspot.com/2018/12/how-to-write-cv.html"

# query the website and return the html to the variable ‘page’
page = urlopen(quote_page)

# parse the html using beautiful soup and store in variable `soup`
soup = BeautifulSoup(page, "html.parser")

# Take out the <div> of name and get its value
date_value = soup.find('h2', attrs={'class':'date-header'}) #Date of the post
main_header_value = soup.find('h3', attrs={'class': 'post-title entry-title'}) #main header title

 # strip() is used to remove starting and trailing
date_string = date_value.text.strip()
main_header_string = main_header_value.text.strip()

print ("Date of the post "+ date_string)
print ("Received data: "+ main_header_string)

