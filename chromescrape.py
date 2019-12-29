from selenium import webdriver
from time import sleep
from selenium.webdriver.common.keys import Keys
# chromedriver = webdriver.Chrome(executable_path = 'C:\Users\VENKATESH\Downloads\chromedriver_win32'')
chromedriver=webdriver.Chrome()
url = "https://twitter.com/hemanth"
chromedriver.get(url)
sleep(3)
# tweets=chromedriver.find_element_by_xpath('//*[@class="TweetTextSize TweetTextSize--normal js-tweet-text tweet-text"]/text()')).text
# print(tweets)