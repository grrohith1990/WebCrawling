from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains


for i in range(7, 28):
    driver = webdriver.Firefox()
    driver.get("http://www.babynamesdirect.com/indian-baby-names/")
    main_window = driver.current_window_handle
    action = ActionChains(driver)
    alphabet = driver.find_element_by_xpath("/html/body/div[2]/nav[2]/ul[2]/li[%s]/a" %str(i))
    _file = open('all_indian_girls_names_startinf_with_%s.txt' %str(alphabet.text), "w")
    action.key_down(Keys.CONTROL).click(alphabet)
    action.perform()
    alphabet.send_keys(Keys.CONTROL + Keys.TAB)
    driver.switch_to_window(main_window)
    count = 1
    except_count = 0
    while(True):
        try:
            name = driver.find_element_by_xpath("/html/body/div[2]/div[6]/div[2]/table/tbody/tr[%s]/td[2]/b" %str(count))
            print name.text
            _file.write(name.text)
            _file.write('\n')
            count += 1
        except Exception:
            count += 1
            except_count += 1
            if except_count > 6:
                try:
                    _next = driver.find_element_by_xpath("/html/body/div[2]/nav[3]/div[2]/a")
                    if _next.text.split(' ')[2] == 'Next':
                        _next.click()
                        count = 1
                        except_count = 0
                        driver.find_element_by_tag_name('body').send_keys(Keys.CONTROL + 'w')
                        driver.switch_to_window(main_window)
                        pass
                    else:
                        driver.close()
                        break
                except:
                    break
            pass