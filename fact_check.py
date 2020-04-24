from selenium import webdriver
import time

def search_the_text(line):
    
    print('\n\n\t Searching for ',line, 'in the internet')

    #input_text = input('\n \tType a US news to fact check : ')

    input_text = line

    print('\n\n\tLoading the Fact checking sites...')

    option = webdriver.FirefoxOptions()

    option.add_argument('--headless')


    driver = webdriver.Firefox(options=option)
    driver.get('https://www.snopes.com/')

    driver.maximize_window()
    print('\n\n\tSearching the news in Fact checking sites...')

    driver.find_element_by_xpath('//*[@id="header-search"]').send_keys(input_text)
    driver.find_element_by_xpath('/html/body/div[2]/header/nav/div/div/div/form/button').click()

    result = driver.find_element_by_xpath('/html/body/div[3]/div/div/main').text

    if 'no result' in result:
        driver.close()
        print('no result found!')

    headline = driver.find_element_by_xpath('/html/body/div[3]/div/div/main/div/div[3]/div/div[1]/a')
    news_headline = headline.get_attribute('title')

    print('\n\n\tNEWS HEADLINE -> ', news_headline , '\n\n')

    link = driver.find_element_by_xpath('/html/body/div[3]/div/div/main/div/div[3]/div/div[1]/a')

    linkString = link.get_attribute('href')

    driver.find_element_by_xpath('/html/body/div[3]/div/div/main/div/div[3]/div/div[1]/a/h2').click()

    print('\tClaim\n')
    print('\t',driver.find_element_by_xpath('/html/body/div[4]/div/div/main/article/div[3]/div/p').text,'\n\n')

    try:
        ele = driver.find_element_by_xpath('/html/body/div[4]/div/div/main/article/div[4]/div/div/div').text

        print('\t Fact Check')

        if 'True' in ele:
            print('\tThe news is True')
        elif 'False' in ele:
            print('\tThe news is False')
        else:
            print('The news is mixture (means some points are wrong some points are right)')

        print('\n\n\t Want to know more go to this link :\n\t',linkString,'\n\n')
           
    except:
        print("The news cannot be found on the Fact Checking websites. Lets do some anlysis of the content!")
        time.sleep(10)
        driver.quit()

    time.sleep(10)
    driver.quit()


