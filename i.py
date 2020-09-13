'''

code by @sudoreboot2020





vk: vk.com/sudoreboot2020






github : github.com/kotik06







'''
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
import pyautogui as p
import os
import time

try:
    import cfg
except:
    pass


def banner():
    print("""
    
    
    
    oooooooooo.    oooooooooooo oooooooooooo ooooo      ooo 
    `888'   `Y8b  d'""""""d888' `888'     `8 `888b.     `8' 
     888      888       .888P    888          8 `88b.    8  
     888      888      d888'     888oooo8     8   `88b.  8  
     888      888    .888P       888    "     8     `88b.8  
     888     d88'   d888'    .P  888       o  8       `888  
    o888bood8P'   .8888888888P  o888ooooood8 o8o        `8  
                                                        
                                                            
    
    """)

def prosmotri():
    file = str(input('Название файла с аккаунтами (по умолчанию "1-100.txt"):'))
    n = int(input('Количество просмотров (целое число):'))
    n_2=int(input('Количество нажатиq на PAGE_DOWN(зависит от длины статьи||целое число): '))
    link = input('Ссылка :')
    # link='https://zen.yandex.ru/media/id/5f19904590d2f3540f36aeb8/test-5f1990560416415eeed360fb'#ссылка на статью
    if file == '' or file == " ":
        file = '1-100.txt'
    f = open(file, 'r', encoding='utf-8')
    abc = f.readlines()
    account = [line.rstrip() for line in abc]
    print(len(account), ' аккаунтов в файле')

    for i in range(n):
        driver = webdriver.Chrome(executable_path=cfg.path)  # запуск хрома
        a = account[i].split(';')
        login = a[0]
        passwd = a[1]
        print("авторизация с аккаунта :", login, passwd)  # выводит логин+пароль в консоль
        driver.set_window_size(800, 600)
        driver.get(link)  # открытие ссылки
        driver.find_element_by_xpath('//*[@id="header-container"]/div/div[2]/div/nav/div[3]/button[2]').click()  # клик по Войти
        wait = WebDriverWait(driver, 10)
        search = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="passp-field-login"]')))
        search.clear()
        search.send_keys(login)
        search.send_keys(Keys.ENTER)
        time.sleep(5)
        driver.find_element_by_xpath('//*[@id="passp-field-passwd"]').send_keys(passwd)
        time.sleep(2)
        driver.find_element_by_xpath('//*[@id="root"]/div/div/div[2]/div/div/div[3]/div[2]/div/div[1]/form/div[3]/button').click()
        time.sleep(5)

        for i in range(n_2):
            driver.find_element_by_tag_name('body').send_keys(Keys.PAGE_DOWN)  # скроллинг
            time.sleep(10)
        for i in range(n_2):
            driver.find_element_by_tag_name('body').send_keys(Keys.PAGE_UP)  # скроллинг
            time.sleep(1)
        time.sleep(5)
        search_2 = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="header-container"]/div/div[2]/div/nav/div[3]/div[3]/button')))  # ВЫХОД
        search_2.click()
        time.sleep(5)
        search_3 = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="header-container"]/div/div[2]/div/nav/div[3]/div[4]/div/div[3]/a')))
        search_3.click()
        # driver.close()
        driver.quit()  # выход


def likes():
    file = str(input('Название файла с аккаунтами (по умолчанию "1-100.txt"):'))
    link = input('Ссылка :')
    n = int(input('Количество просмотров (целое число):'))
    n_2=int(input('Количество нажатиq на PAGE_DOWN(зависит от длины статьи||целое число): '))
    # link='https://zen.yandex.ru/media/id/5f19904590d2f3540f36aeb8/test-5f1990560416415eeed360fb'#ссылка на статью
    if file == '' or file == " ":
        file = '1-100.txt'
    f = open(file, 'r', encoding='utf-8')
    abc = f.readlines()
    account = [line.rstrip() for line in abc]
    print(len(account), ' аккаунтов в файле')

    for i in range(n):
        driver = webdriver.Chrome(executable_path=cfg.path)  # запуск хрома
        a = account[i].split(';')
        login = a[0]
        passwd = a[1]
        print("авторизация с аккаунта :", login, passwd)  # выводит логин+пароль в консоль
        driver.set_window_size(800, 600)
        driver.get(link)  # открытие ссылки
        driver.find_element_by_xpath('//*[@id="header-container"]/div/div[2]/div/nav/div[3]/button[2]').click()  # клик по Войти
        wait = WebDriverWait(driver, 10)
        search = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="passp-field-login"]')))
        search.clear()
        search.send_keys(login)
        search.send_keys(Keys.ENTER)
        time.sleep(5)
        driver.find_element_by_xpath('//*[@id="passp-field-passwd"]').send_keys(passwd)
        time.sleep(2)
        driver.find_element_by_xpath( '//*[@id="root"]/div/div/div[2]/div/div/div[3]/div[2]/div/div[1]/form/div[3]/button').click()
        time.sleep(5)

        for i in range(n_2):
            driver.find_element_by_tag_name('body').send_keys(Keys.PAGE_DOWN)  # скроллинг
            time.sleep(10)
        for i in range(n_2):
            driver.find_element_by_tag_name('body').send_keys(Keys.PAGE_UP)  # скроллинг
            time.sleep(1)
        time.sleep(5)
        driver.find_element_by_xpath('//*[@id="article__left"]/div/div/div/div[1]/div[1]/div[1]/button').click()#лайк
        time.sleep(5)
        search_2 = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="header-container"]/div/div[2]/div/nav/div[3]/div[3]/button')))#ВЫХОД
        search_2.click()
        time.sleep(5)
        search_3 = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="header-container"]/div/div[2]/div/nav/div[3]/div[4]/div/div[3]/a')))
        search_3.click()
        #driver.close()
        driver.quit()  # выход


def main():
    banner()
    m = str(input('[1]-лайки+просмотры\n[2]-просмотры\n[3]-создание конфиг файла\n[4]-об авторе\n[-->]'))

    if m == '1':
        likes()
    elif m == '2':
        prosmotri()
    elif m == '3':
        print('[1]-откройте файл "cfg.py"\n[2]-на 1 линии в ковычки впишите АБСОЛЮТНЫЙ путь к файлу "chromedriver.exe"(прим.: C:\Dzen\chromedriver.exe)\n[3]-сохраните и закройте\n[4]-перезапустите программу')
        time.sleep(30)
    elif m == '4':
        print("vk.com/sudoreboot2020\nlolz.guru/members/1005970\ngithub.com/kotik06\nАвтор не несет ответственности за причиненный Вами ущерб.\n")
        time.sleep(30)

if __name__ == '__main__':
    main()
