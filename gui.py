from guizero import App,PushButton,Box
from selenium import webdriver
chrome_path=r"C:\Users\User\Desktop\chromedriver_win32 (5)\chromedriver.exe"
driver=webdriver.Chrome(chrome_path)
driver.get("https://www.python.org/")
def test():
    driver.find_element_by_xpath("""//*[@id="downloads"]/a""").click()
def set():
    driver.find_element_by_xpath("""//*[@id="documentation"]/a""").click()
def ready():
    driver.find_element_by_xpath("""//*[@id="community"]/a""").click()
def go():
     driver.find_element_by_xpath("""//*[@id="success-stories"]/a""").click()
app=App()
buttons_box = Box(app)
button1=PushButton(buttons_box,text="↑",align="top",command=test)
button2=PushButton(buttons_box,text="⟵",align="left",command=set)
button3=PushButton(buttons_box,text="⟶",pady=10,padx=10,align="right",command=ready)
button4=PushButton(buttons_box,text="↓",align="bottom",command=go)
button5=PushButton(buttons_box,text="stop",align="bottom")
app.display()
