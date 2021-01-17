from selenium import webdriver

from selenium.webdriver import ActionChains #滑动
from selenium.webdriver.common.by import By #选择器
from selenium.webdriver.common.by import By #按照什么方式查找，By.ID,By.CSS_SELECTOR
from selenium.webdriver.common.keys import Keys #键盘按键操作


browser = webdriver.Chrome()
browser.get('https://buff.163.com/market/goods?goods_id=42964&from=market')
#str = browser.find_element_by_class_name('t_Left').find_element_by_tag_name('div').find_element_by_class_name('f_Strong').text
str2 = browser.find_element_by_tag_name('body')
print(str2)