from typing import Optional
import telebot
import config
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from datetime import datetime, timedelta
options = webdriver.ChromeOptions()
options.add_argument('--headless')
driver = webdriver.Chrome(
    executable_path='drivers/chromedriver', chrome_options=options)
bot = telebot.TeleBot(config.TOKEN)

days = []


def check_exists_by_xpath(xpath):
    try:
        driver.find_element_by_css_selector(xpath)
    except NoSuchElementException:
        return False
    return True


def parse():
    URL = 'https://ua.sinoptik.ua/погода-рівне'
    driver.get(URL)
    currentDay = driver.find_element_by_css_selector(
        '#bd1 .day-link').text.strip()
    sec = driver.find_element_by_css_selector(
        '#bd2 .day-link').text.strip()
    thr = driver.find_element_by_css_selector(
        '#bd3 .day-link').text.strip()
    four = driver.find_element_by_css_selector(
        '#bd4 .day-link').text.strip()
    five = driver.find_element_by_css_selector(
        '#bd5 .day-link').text.strip()
    six = driver.find_element_by_css_selector(
        '#bd6 .day-link').text.strip()
    seven = driver.find_element_by_css_selector(
        '#bd7 .day-link').text.strip()

    days.extend([currentDay, sec, thr, four, five, six, seven])


parse()
d = datetime.now()


@bot.message_handler(commands=['start'])
def start_message(message):
    keyboard = telebot.types.ReplyKeyboardMarkup(True)
    keyboard.row('/start', '/days')
    bot.send_message(
        message.chat.id, 'Hello!\nI am WeatherBot\nClick command /days!!', reply_markup=keyboard)


@bot.message_handler(commands=['days'])
def buttons(message):
    markup = telebot.types.InlineKeyboardMarkup()
    markup.add(telebot.types.InlineKeyboardButton(
        text=f'{days[0]}', callback_data=1))
    markup.add(telebot.types.InlineKeyboardButton(
        text=f'{days[1]}', callback_data=2))
    markup.add(telebot.types.InlineKeyboardButton(
        text=f'{days[2]}', callback_data=3))
    markup.add(telebot.types.InlineKeyboardButton(
        text=f'{days[3]}', callback_data=4))
    markup.add(telebot.types.InlineKeyboardButton(
        text=f'{days[4]}', callback_data=5))
    markup.add(telebot.types.InlineKeyboardButton(
        text=f'{days[5]}', callback_data=6))
    markup.add(telebot.types.InlineKeyboardButton(
        text=f'{days[6]}', callback_data=7))
    bot.send_message(
        message.chat.id, text='Виберіть день тижня на якій ви бажаєте подивитись погоду', reply_markup=markup)


@bot.callback_query_handler(func=lambda call: True)
def query_handler(call):
    bot.answer_callback_query(
        callback_query_id=call.id, text='Трішки зачекайте')
    answer = ''
    if call.data == '1':
        end_date = d
        month = '%02d' % end_date.month
        day = '%02d' % end_date.day
        URL = f'https://ua.sinoptik.ua/погода-рівне/{end_date.year}-{month}-{day}'
        driver.get(URL)
        min_temp = driver.find_element_by_css_selector(
            '.temperature .min').text.strip().replace('\n', ' ')
        max_temp = driver.find_element_by_css_selector(
            '.temperature .max').text.strip().replace('\n', ' ')
        desc = driver.find_element_by_css_selector(
            '.wDescription .description').text.strip().replace('\n', ' ')
        today = driver.find_element_by_css_selector(
            '.today-temp').text.strip().replace('\n', ' ')
        wind = driver.find_element_by_css_selector(
            '.cur .wind').get_attribute('data-tooltip')
        if check_exists_by_xpath('.oWarnings'):
            warning = driver.find_element_by_css_selector(
                '.oWarnings .description').text.strip().replace('\n', ' ')
        else:
            warning = 'Узбагойся'
        vol = driver.find_element(
            By.XPATH, '//table[@class = "weatherDetails"]/tbody/tr[6]')
        curvol = vol.find_element_by_css_selector('.cur').text
        answer = f'{min_temp}\n{max_temp}\n{desc}\nВітер: {wind} \nПопередження: {warning}\nВологість: {curvol}'
    elif call.data == '2':
        end_date = d + timedelta(days=1)
        month = '%02d' % end_date.month
        day = '%02d' % end_date.day
        URL = f'https://ua.sinoptik.ua/погода-рівне/{end_date.year}-{month}-{day}'
        driver.get(URL)
        min_temp = driver.find_element_by_css_selector(
            '#bd2 .temperature .min').text.strip().replace('\n', ' ')
        max_temp = driver.find_element_by_css_selector(
            '#bd2 .temperature .max').text.strip().replace('\n', ' ')
        desc = driver.find_element_by_css_selector(
            '.wDescription .description').text.strip().replace('\n', ' ')
        wind = driver.find_element_by_css_selector(
            '.wind').get_attribute('data-tooltip')
        if check_exists_by_xpath('.oWarnings'):
            warning = driver.find_element_by_css_selector(
                '.oWarnings .description').text.strip().replace('\n', ' ')
        else:
            warning = 'Узбагойся'
        vol = driver.find_element(
            By.XPATH, '//table[@class = "weatherDetails"]/tbody/tr[6]/td').text

        answer = f'{min_temp}\n{max_temp}\n{desc}\nВітер: {wind} \nПопередження: {warning}\nВологість: {vol}'
    elif call.data == '3':
        end_date = d + timedelta(days=2)
        month = '%02d' % end_date.month
        day = '%02d' % end_date.day
        URL = f'https://ua.sinoptik.ua/погода-рівне/{end_date.year}-{month}-{day}'
        driver.get(URL)
        min_temp = driver.find_element_by_css_selector(
            '#bd3 .temperature .min').text.strip().replace('\n', ' ')
        max_temp = driver.find_element_by_css_selector(
            '#bd3 .temperature .max').text.strip().replace('\n', ' ')
        desc = driver.find_element_by_css_selector(
            '.wDescription .description').text.strip().replace('\n', ' ')
        wind = driver.find_element_by_css_selector(
            '.wind').get_attribute('data-tooltip')
        if check_exists_by_xpath('.oWarnings'):
            warning = driver.find_element_by_css_selector(
                '.oWarnings .description').text.strip().replace('\n', ' ')
        else:
            warning = 'Узбагойся'
        vol = driver.find_element(
            By.XPATH, '//table[@class = "weatherDetails"]/tbody/tr[6]/td').text

        answer = f'{min_temp}\n{max_temp}\n{desc}\nВітер: {wind} \nПопередження: {warning}\nВологість: {vol}'
    elif call.data == '4':
        end_date = d + timedelta(days=3)
        month = '%02d' % end_date.month
        day = '%02d' % end_date.day
        URL = f'https://ua.sinoptik.ua/погода-рівне/{end_date.year}-{month}-{day}'
        min_temp = driver.find_element_by_css_selector(
            '#bd4 .temperature .min').text.strip().replace('\n', ' ')
        max_temp = driver.find_element_by_css_selector(
            '#bd4 .temperature .max').text.strip().replace('\n', ' ')
        desc = driver.find_element_by_css_selector(
            '.wDescription .description').text.strip().replace('\n', ' ')
        wind = driver.find_element_by_css_selector(
            '.wind').get_attribute('data-tooltip')
        if check_exists_by_xpath('.oWarnings'):
            warning = driver.find_element_by_css_selector(
                '.oWarnings .description').text.strip().replace('\n', ' ')
        else:
            warning = 'Узбагойся'
        vol = driver.find_element(
            By.XPATH, '//table[@class = "weatherDetails"]/tbody/tr[6]/td').text

        answer = f'{min_temp}\n{max_temp}\n{desc}\nВітер: {wind} \nПопередження: {warning}\nВологість: {vol}'
    elif call.data == '5':
        end_date = d + timedelta(days=4)
        month = '%02d' % end_date.month
        day = '%02d' % end_date.day
        URL = f'https://ua.sinoptik.ua/погода-рівне/{end_date.year}-{month}-{day}'
        min_temp = driver.find_element_by_css_selector(
            '#bd5 .temperature .min').text.strip().replace('\n', ' ')
        max_temp = driver.find_element_by_css_selector(
            '#bd5 .temperature .max').text.strip().replace('\n', ' ')
        desc = driver.find_element_by_css_selector(
            '.wDescription .description').text.strip().replace('\n', ' ')
        wind = driver.find_element_by_css_selector(
            '.wind').get_attribute('data-tooltip')
        if check_exists_by_xpath('.oWarnings'):
            warning = driver.find_element_by_css_selector(
                '.oWarnings .description').text.strip().replace('\n', ' ')
        else:
            warning = 'Узбагойся'
        vol = driver.find_element(
            By.XPATH, '//table[@class = "weatherDetails"]/tbody/tr[6]/td').text

        answer = f'{min_temp}\n{max_temp}\n{desc}\nВітер: {wind} \nПопередження: {warning}\nВологість: {vol}'
    elif call.data == '6':
        end_date = d + timedelta(days=5)
        month = '%02d' % end_date.month
        day = '%02d' % end_date.day
        URL = f'https://ua.sinoptik.ua/погода-рівне/{end_date.year}-{month}-{day}'
        min_temp = driver.find_element_by_css_selector(
            '#bd6 .temperature .min').text.strip().replace('\n', ' ')
        max_temp = driver.find_element_by_css_selector(
            '#bd6 .temperature .max').text.strip().replace('\n', ' ')
        desc = driver.find_element_by_css_selector(
            '.wDescription .description').text.strip().replace('\n', ' ')
        wind = driver.find_element_by_css_selector(
            '.wind').get_attribute('data-tooltip')
        if check_exists_by_xpath('.oWarnings'):
            warning = driver.find_element_by_css_selector(
                '.oWarnings .description').text.strip().replace('\n', ' ')
        else:
            warning = 'Узбагойся'
        vol = driver.find_element(
            By.XPATH, '//table[@class = "weatherDetails"]/tbody/tr[6]/td').text

        answer = f'{min_temp}\n{max_temp}\n{desc}\nВітер: {wind} \nПопередження: {warning}\nВологість: {vol}'
    elif call.data == '7':
        end_date = d + timedelta(days=6)
        month = '%02d' % end_date.month
        day = '%02d' % end_date.day
        URL = f'https://ua.sinoptik.ua/погода-рівне/{end_date.year}-{month}-{day}'
        min_temp = driver.find_element_by_css_selector(
            '#bd7 .temperature .min').text.strip().replace('\n', ' ')
        max_temp = driver.find_element_by_css_selector(
            '#bd7 .temperature .max').text.strip().replace('\n', ' ')
        desc = driver.find_element_by_css_selector(
            '.wDescription .description').text.strip().replace('\n', ' ')
        wind = driver.find_element_by_css_selector(
            '.wind').get_attribute('data-tooltip')
        if check_exists_by_xpath('.oWarnings'):
            warning = driver.find_element_by_css_selector(
                '.oWarnings .description').text.strip().replace('\n', ' ')
        else:
            warning = 'Узбагойся'
        vol = driver.find_element(
            By.XPATH, '//table[@class = "weatherDetails"]/tbody/tr[6]/td').text

        answer = f'{min_temp}\n{max_temp}\n{desc}\nВітер: {wind} \nПопередження: {warning}\nВологість: {vol}'
    bot.send_message(
        call.message.chat.id, answer)
    bot.edit_message_reply_markup(
        call.message.chat.id, call.message.message_id)


bot.polling()
