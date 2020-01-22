#! /usr/bin/env python
# -*- coding: utf-8 -*-

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.options import Options
from selenium.webdriver import Firefox
from kinopoisk.movie import Movie
films_file = open('films.txt', 'r')
films_spisok = films_file.read().split('\n')
for i in range(len(films_spisok)):
    a = films_spisok[i]
    movie_list = Movie.objects.search('{}'.format(a))

    debug = 1 # 0 to switch off

    opts = Options()
    opts.set_headless()
    assert opts.headless

    def open_brow():
        global debug,driver,wait
        driver = Firefox(options=opts) # not GUI
    #    driver = Firefox() # GUI
        wait = WebDriverWait(driver, 1000)
        driver.get("http://pebod2k8.beget.tech/admin.php")
        if debug == 1:
            print ('Браузер запустился')
    def login():
        wait.until(EC.element_to_be_clickable((By.XPATH, '//input[@name="username"]'))).send_keys(login)
        wait.until(EC.element_to_be_clickable((By.XPATH, '//input[@name="password"]'))).send_keys(password)
        wait.until(EC.element_to_be_clickable((By.XPATH, '//button[@class="btn btn-primary btn-raised btn-block legitRipple"]'))).click()
        if debug == 1:
            print ('Залогинился')


    for i in range(len(movie_list)):
        print('Фильм ' + str(i))
        movie_id = movie_list[i].id
        movie = Movie(id=movie_id)
        movie.get_content('main_page')


        if len(movie.title_en) <= 1:
            nazvanie = str(movie.title)+ ' ' + '('+str(movie.year)+')'
        else:
            nazvanie = str(movie.title)+ ' ' + '('+str(movie.title_en)+')'
        tip = 'фильмы'
        poster = 'https://st.kp.yandex.net/images/film_big/{}.jpg'.format(str(movie_id))

        id2 = movie_id
        if len(movie.countries) == 0:
            strana = 'None'
        else:
            strana = str(', '.join(str(x) for x in movie.countries))
        if len(movie.directors) == 0:
            rejiser = 'None'
        else:
            rejiser = str(', '.join(str(a) for a in movie.directors))
        if len(movie.actors) == 0:
            glav_rol = 'None'
        else:
            glav_rol = str(', '.join(str(z) for z in movie.actors))
        if len(str(movie.year)) <= 1:
            god = '-'
        else:
            god = movie.year
        raiting = movie.rating
        if len(movie.plot) <= 1:
            opisanie = '-'
        else:
            opisanie = movie.plot
        if len(movie.genres) == 0:
            janr == 'None'
        else:
            janr = str(', '.join(str(b) for b in movie.genres))

        def add_news():
            print (nazvanie)
            wait.until(EC.element_to_be_clickable((By.XPATH, '//a[@class="btn btn-link btn-float text-size-small has-text legitRipple"]'))).click()
            wait.until(EC.element_to_be_clickable((By.XPATH, '//input[@id="title"]'))).send_keys(nazvanie)
            if debug == 1:
                print ('Название +')
            wait.until(EC.element_to_be_clickable((By.XPATH, '//input[@class="chosen-search-input default"]'))).click()
            wait.until(EC.element_to_be_clickable((By.XPATH, '//input[@class="chosen-search-input default"]'))).send_keys(tip + Keys.RETURN)
            if debug == 1:
                print ('Тип +')
            wait.until(EC.element_to_be_clickable((By.XPATH, '//input[@id="xf_grab-janr"]'))).send_keys(janr)
            if debug == 1:
                print ('Жанр +')
            wait.until(EC.element_to_be_clickable((By.XPATH, '//div[@class="fr-element fr-view"]'))).send_keys(poster)
            if debug == 1:
                print ('Постер +')
            wait.until(EC.element_to_be_clickable((By.XPATH, '//input[@id="xf_grab-opisanie"]'))).send_keys(opisanie)
            if debug == 1:
                print ('Описание +')
            wait.until(EC.element_to_be_clickable((By.XPATH, '//input[@id="xf_kinopoisk"]'))).send_keys(id2)
            if debug == 1:
                print ('Айди +')
            wait.until(EC.element_to_be_clickable((By.XPATH, '//input[@id="xf_grab-country"]'))).send_keys(strana)
            if debug == 1:
                print ('Страна +')
            wait.until(EC.element_to_be_clickable((By.XPATH, '//input[@id="xf_grab-director"]'))).send_keys(rejiser)
            if debug == 1:
                print ('Режисер +')
            wait.until(EC.element_to_be_clickable((By.XPATH, '//input[@id="xf_grab-actors"]'))).send_keys(glav_rol)
            if debug == 1:
                print ('Главные актеры +')

            try:
                wait.until(EC.element_to_be_clickable((By.XPATH, '//input[@id="xf_grab-year"]'))).send_keys(god)
            except TypeError:
                print ('########## TypeError ##########')
                wait.until(EC.element_to_be_clickable((By.XPATH, '//input[@id="xf_grab-year"]'))).send_keys('-')
            finally:
                if debug == 1:
                    print ('Год +')

            wait.until(EC.element_to_be_clickable((By.XPATH, '//input[@id="xf_grab-rating"]'))).send_keys(str(raiting))
            if debug == 1:
                print ('Рейтинг +')
            if debug == 1:
                print ('Все данные успешно ввелись')
            wait.until(EC.element_to_be_clickable((By.XPATH, '//button[@class="btn bg-teal btn-sm btn-raised position-left legitRipple"]'))).click()

        if __name__ == '__main__':
            login = str(input ('Login: '))
            password = str(input ('Password: '))
            open_brow()
            login()
            add_news()
            driver.close()
