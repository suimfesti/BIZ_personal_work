from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup
import pandas as pd
from pandas import DataFrame
import time

#1. 따릉이 시민의견 게시판 사이트에서 문의사항 제목을 크롤링해보자

 # chrome driver 설정
driver = webdriver.Chrome('C:/Users/최수임/Downloads/chromedriver_win32/chromedriver.exe')
driver.implicitly_wait(10)

url = "https://www.bikeseoul.com/customer/opinionBoard/opinionBoardList.do?currentPageNo=1"

driver.get(url)
html = driver.page_source
soup = BeautifulSoup(html, 'html.parser')

# title crawling
title = WebDriverWait(driver, 20) \
    .until(EC.presence_of_element_located((By.CSS_SELECTOR, "#sub > div.container > div > div > div.board_box > table > tbody > tr:nth-child(2) > td.left > a")))

print("Title: {}".format(title.text))

#2. Text Crawling with for loop
 # chrome driver 설정
driver = webdriver.Chrome('C:/Users/최수임/Downloads/chromedriver_win32/chromedriver.exe')
driver.implicitly_wait(10)

url = "https://www.bikeseoul.com/customer/opinionBoard/opinionBoardList.do?currentPageNo=1"

driver.get(url)
html = driver.page_source
soup = BeautifulSoup(html, 'html.parser')

# title crawling
for i in range(2, 7):
    title = WebDriverWait(driver, 20) \
        .until(EC.presence_of_element_located((By.CSS_SELECTOR, "#sub > div.container > div > div > div.board_box > table > tbody > tr:nth-child(" + str(i) + ") > td.left > a")))
    print("Title: {}".format(title.text))

# chrome driver 설정
driver = webdriver.Chrome('C:/Users/최수임/Downloads/chromedriver_win32/chromedriver.exe')
driver.implicitly_wait(10)

url = "https://www.bikeseoul.com/customer/opinionBoard/opinionBoardList.do?currentPageNo=1"

driver.get(url)
html = driver.page_source
soup = BeautifulSoup(html, 'html.parser')

# 빈 리스트 변수
title_list = []

# title crawling
for i in range(2, 7):
    title = WebDriverWait(driver, 20) \
        .until(EC.presence_of_element_located((By.CSS_SELECTOR, "#sub > div.container > div > div > div.board_box > table > tbody > tr:nth-child(" + str(i) + ") > td.left > a")))
    title_list.append(title.text)
    
print(title_list)

#3. text crawling(click&back)
 # chrome driver 설정
driver = webdriver.Chrome('C:/Users/Hansol/Downloads/chromedriver_win32/chromedriver.exe')
driver.implicitly_wait(10)

url = "https://www.bikeseoul.com/customer/opinionBoard/opinionBoardList.do?currentPageNo=1"

driver.get(url)
html = driver.page_source
soup = BeautifulSoup(html, 'html.parser')

# click
click_element = WebDriverWait(driver, 20) \
    .until(EC.presence_of_element_located((By.CSS_SELECTOR, "#sub > div.container > div > div > div.board_box > table > tbody > tr:nth-child(2) > td.left > a")))
click_element.click()    

# back
driver.back()

#4. Text Crawling including contents
 # chrome driver 설정
driver = webdriver.Chrome('C:/Users/최수임/Downloads/chromedriver_win32/chromedriver.exe')
driver.implicitly_wait(10)

url = "https://www.bikeseoul.com/customer/opinionBoard/opinionBoardList.do?currentPageNo=1"
driver.get(url)
html = driver.page_source
soup = BeautifulSoup(html, 'html.parser')

# 빈 리스트 변수
title_list = []
content_list = []

# title crawling
for i in range(2, 7):
    # click
    click_element = WebDriverWait(driver, 20) \
        .until(EC.presence_of_element_located((By.CSS_SELECTOR, "#sub > div.container > div > div > div.board_box > table > tbody > tr:nth-child("+str(i)+") > td.left > a")))
    click_element.click()    

    # title crawling
    title = WebDriverWait(driver, 20).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, "#sub > div.container > div > div > div.read_box > dl > dt > p")))
    title_list.append(title.text)
    
    # content crawling
    content = WebDriverWait(driver, 20).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, "body > div.wrap.board > div.container > div > div > div.read_box > dl > dd")))
    content_list.append(content.text)
    
    # back
    driver.back()
    
print(title_list)
print(content_list)

#데이터프레임 저장
 # chrome driver 설정
driver = webdriver.Chrome('C:/Users/최수임/Downloads/chromedriver_win32/chromedriver.exe')
driver.implicitly_wait(10)

url = "https://www.bikeseoul.com/customer/opinionBoard/opinionBoardList.do?currentPageNo=1"
driver.get(url)
html = driver.page_source
soup = BeautifulSoup(html, 'html.parser')

# 빈 리스트 변수
title_list = []
content_list = []

# title crawling
for i in range(2, 7):
    # click
    click_element = WebDriverWait(driver, 20) \
        .until(EC.presence_of_element_located((By.CSS_SELECTOR, "#sub > div.container > div > div > div.board_box > table > tbody > tr:nth-child("+str(i)+") > td.left > a")))
    click_element.click()    

    # title crawling
    title = WebDriverWait(driver, 20).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, "#sub > div.container > div > div > div.read_box > dl > dt > p")))
    title_list.append(title.text)
    
    # content crawling
    content = WebDriverWait(driver, 20).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, "body > div.wrap.board > div.container > div > div > div.read_box > dl > dd")))
    content_list.append(content.text)
    
    # back
    driver.back()
    
    
    
# 결과 변수
raw_result = {'title': title_list,
          'content': content_list}

result = pd.DataFrame(raw_result)

# csv 파일로 save
result.to_csv("BikeTest1", mode='w')

# driver 종료
driver.quit()


#5. Text Crawling with double for loop
# chrome driver 설정
driver = webdriver.Chrome('C:/Users/최수임/Downloads/chromedriver_win32/chromedriver.exe')
driver.implicitly_wait(10)

# 빈 리스트 변수
title_list = []
content_list = []

# 1page ~ 5page 크롤링
for page in range(1, 6):

    url = "https://www.bikeseoul.com/customer/opinionBoard/opinionBoardList.do?currentPageNo=" + str(page)
    driver.get(url)
    html = driver.page_source
    soup = BeautifulSoup(html, 'html.parser')


    # title crawling
    for i in range(2, 7):
        # click
        click_element = WebDriverWait(driver, 20) \
            .until(EC.presence_of_element_located((By.CSS_SELECTOR, "#sub > div.container > div > div > div.board_box > table > tbody > tr:nth-child("+str(i)+") > td.left > a")))
        click_element.click()    

        # title crawling
        title = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "#sub > div.container > div > div > div.read_box > dl > dt > p")))
        title_list.append(title.text)

        # content crawling
        content = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "body > div.wrap.board > div.container > div > div > div.read_box > dl > dd")))
        content_list.append(content.text)

        # back
        driver.back()
    
    
# 결과 변수
raw_result2 = {'title': title_list,
          'content': content_list}

result2 = pd.DataFrame(raw_result2)

# csv 파일로 save
result2.to_csv("BikeTest2", mode='w')

# driver 종료
driver.quit()

result2

# 6. Text Crawling with function (심화)
def BikeDataCrawler(starting_page, end_page):
    # chrome driver 설정
    driver = webdriver.Chrome('C:/Users/최수임/Downloads/chromedriver_win32/chromedriver.exe')
    driver.implicitly_wait(10)

    # 빈 리스트 변수
    title_list = []
    content_list = []

    # url에 page가 있는 특성에 따라 for문 생성
    for page in range(starting_page, end_page+1):

        # 따릉이 url 설정
        url = "https://www.bikeseoul.com/customer/opinionBoard/opinionBoardList.do?currentPageNo=" + str(page)
        driver.get(url)
        html = driver.page_source
        soup = BeautifulSoup(html, 'html.parser')

        # 페이지마다 5개 글 크롤링
        for i in range(2, 7):
            # click
            click_element = WebDriverWait(driver, 20) \
                .until(EC.presence_of_element_located((By.CSS_SELECTOR, "#sub > div.container > div > div > div.board_box > table > tbody > tr:nth-child("+str(i)+") > td.left > a")))
            click_element.click()    

            # title crawling
            title = WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, "#sub > div.container > div > div > div.read_box > dl > dt > p")))
            title_list.append(title.text)

            # content crawling
            content = WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, "body > div.wrap.board > div.container > div > div > div.read_box > dl > dd")))
            content_list.append(content.text)

            # back
            driver.back()
        
        # page check
        print(str(page)+"페이지 크롤링 완료!")

    # 결과 변수
    raw_result = {'title': title_list,
              'content': content_list}

    result = pd.DataFrame(raw_result)
    
    # csv 파일로 save
    result.to_csv("BikeData.csv", mode='w')
    
    # driver 종료
    driver.quit()
    
    # return
    return result

data = BikeDataCrawler(starting_page = 1, end_page = 5)
data
