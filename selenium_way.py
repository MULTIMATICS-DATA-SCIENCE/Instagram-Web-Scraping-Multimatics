from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time, urllib.request
import requests
from selenium.common.exceptions import NoSuchElementException


def InstaScrap(account, pssword, target, driver):
    # Open Web Browser and Load Instagram, Example: Firefox
    driver.get("https://www.instagram.com/")
    
    # login
    time.sleep(5)
    username=driver.find_element_by_css_selector("input[name='username']")
    password=driver.find_element_by_css_selector("input[name='password']")
    username.clear()
    password.clear()
    username.send_keys(account)
    password.send_keys(pssword)
    login = driver.find_element_by_css_selector("button[type='submit']").click()

    # save your login info?
    time.sleep(10)
    notnow = driver.find_element_by_xpath("//button[contains(text(), 'Not Now')]").click()
    # turn on notif
    time.sleep(10)
    notnow2 = driver.find_element_by_xpath("//button[contains(text(), 'Not Now')]").click()

    # searchbox
    time.sleep(5)
    searchbox=driver.find_element_by_css_selector("input[placeholder='Search']")
    searchbox.clear()
    searchbox.send_keys(target)
    time.sleep(5)
    searchbox.send_keys(Keys.ENTER)
    time.sleep(5)
    searchbox.send_keys(Keys.ENTER)

    # scroll and take url post
    scrolldown=driver.execute_script("window.scrollTo(0, document.body.scrollHeight);var scrolldown=document.body.scrollHeight;return scrolldown;")
    match=False
    posts = []
    
    while(match==False):
        last_count = scrolldown
        time.sleep(10)

        links = driver.find_elements_by_tag_name('a')
        for link in links:
            post =  link.get_attribute('href')
            if '/p/' in post:
                if post in posts:
                    pass
                else:
                    posts.append(post)

        scrolldown = driver.execute_script("window.scrollTo(0, document.body.scrollHeight);var scrolldown=document.body.scrollHeight;return scrolldown;")

        if last_count==scrolldown:
            match=True

    # Extract Data post from Instagram
    for post in posts:
        driver.get(post)
        time.sleep(5)
        try:
            likes = driver.find_element_by_class_name('zV_Nj') # Class for likes
            num_likes = likes.find_element_by_tag_name('span')
            num_likes = num_likes.text
            print("Post with URL: {} have Number of Likes: {}".format(post,num_likes))
        except NoSuchElementException:
            views = driver.find_element_by_class_name('vcOH2')
            num_views = views.find_element_by_tag_name('span')
            num_views = num_views.text
            print("Post with URL: {} have Number of Likes Views".format(post, num_views))
            continue

    print(posts)
    print(len(posts))

    driver.close()

if __name__ == "__main__":
    PATH = r"D:/Project/instagram_scrap"

    account = "weeeebscrap"
    password = "!1q@2w3e4r5T"
    target = "multimatics"
    driver = webdriver.Firefox(PATH)

    result = InstaScrap(account, password, target, driver)