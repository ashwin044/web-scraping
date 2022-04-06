from bs4 import BeautifulSoup
from selenium import webdriver
import pandas as pd

def create_browser(webdriver_path):

    #create a selenium object that mimics the browser
    browser_options = webdriver.ChromeOptions()
    #headless tag created an invisible browsercls
    browser_options.add_argument("--headless")
    browser_options.add_argument('--no-sandbox')
    browser = webdriver.Chrome(executable_path= webdriver_path, chrome_options=browser_options)
    print("Done Creating Browser")
    
    return browser

url = "https://www.naukri.com/python-jobs?k=python"
browser = create_browser('F:\py practice\chromedriver.exe') #Directory of the chrome driver
browser.get(url)
soup = BeautifulSoup(browser.page_source,'lxml')
print(soup.prettify())
browser.close()

df = pd.DataFrame(columns=['Title','Company','Ratings','Reviews','URL'])  #creating a dataframe to save web scraped data 

results = soup.find('div',class_='list')
jobs = results.find_all('article',class_='jobTuple bgWhite br4 mb-8')

for job in jobs:
    # URL to apply for the job 
    URL = job.find('a',class_='title fw500 ellipsis').get('href') 
    print (URL)
    #Job titile 
    Title = job.find('a',class_='title fw500 ellipsis') 
    print (Title. text)
    #company name
    Company = job.find('a',class_='subTitle ellipsis fleft')
    print (Company.text)
    #Rating Counts
    rating_span = job.find('span', class_='starRating fleft dot') 
    if rating_span is None:
        continue 
    else:
        Ratings = rating_span.text 
    print(Ratings)
        # Reviews Counts 
    Review_span = job.find('a',class_='reviewsCount ml-5 fleft blue-text') 
    if Review_span is None:
        continue 
    else:
        Reviews = Review_span. text 
    print(Reviews)
    print(" "*2)
    # Appending data to the Data Frame 
    df=df.append({ 'URL':URL, 'Title':Title. text, 'Company': Company.text, 'Ratings': Ratings, 'Reviews':Reviews},ignore_index = True)
    
df.to_csv("Naukri.com_Data.csv",index=False)