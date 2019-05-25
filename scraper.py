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

#Getting the body parts 

soupTwo = BeautifulSoup('<span style="font-size: large;">What is a CV?</span>',  'html.parser')
titleOne= soupTwo.span.text.strip()#First Subtitle

post_first_para_top = soup.find('blockquote',attrs={'class': 'tr_bq'})
One_para_quote = post_first_para_top.text.strip()

soupThree = BeautifulSoup('<span style="font-size: large;">What to include in a CV ?</span>',  'html.parser')
titleSec= soupThree.span.text.strip()#Second Subtitle

soupFour = BeautifulSoup('<span style="font-size: large;">What not to include ?</span>',  'html.parser')
titleThird= soupFour.span.text.strip()#Third Subtitle

soupFive= BeautifulSoup('<span style="font-size: large;">An important fact</span>',  'html.parser')
titleFour= soupFive.span.text.strip()#Fourth Subtitle


#Whole article at once
One_para_inne = soup.find('div',attrs={'id':'post-body-1322918833010608425' })
test_text = One_para_inne.text.strip()

print ("\nDate of the post : "+ date_string)
print ("\nPost name : "+ main_header_string)

print ("\n "+ titleOne)
print ("\t "+ One_para_quote)
print (" "+ titleSec)
print (" "+ titleThird)
print (" "+ titleFour)


print("\n\n\t\t\t\t\t*******************Whole article at once***********************")
print ("\n "+ test_text)

