import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from colorama import init, Fore, Back
init(autoreset= True)

options = webdriver.ChromeOptions()
options.add_experimental_option('excludeSwitches', ['enable-logging'])

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
driver.maximize_window()
driver.get('https://shop.samsung.com/ar/')
time.sleep(5)

driver.find_element(By.ID, "truste-consent-button").click()
driver.find_element(By.XPATH, "/html/body/div[3]/div[1]/div/div/section/div[1]/button").click()
driver.find_element(By.XPATH, '//*[@id="headerSamsung"]/div[2]/div/div/div[1]/a[2]').click()
time.sleep(2)

usuario = driver.find_element(By.XPATH, "/html/body/div[2]/div/div[1]/div/div[2]/div/div/div/div[2]/div/div/form/div[1]/label/div/input")
usuario.send_keys("gimealvarez2000@gmail.com")
usuario.send_keys(Keys.TAB)
time.sleep(5)

contrasenia = driver.find_element(By.XPATH, "/html/body/div[2]/div/div[1]/div/div[2]/div/div/div/div[2]/div/div/form/div[2]/div/label/div/input")
contrasenia.send_keys("Gimena00")
contrasenia.send_keys(Keys.ENTER)
time.sleep(10)

barra_busqueda = driver.find_element(By.XPATH, "/html/body/div[2]/div/div[1]/div/div[1]/div[2]/div/div/div[1]/a[1]")
barra_busqueda.click()
time.sleep(5)

buscar_elemento = driver.find_element(By.XPATH, "/html/body/div[2]/div/div[1]/div/div[1]/div[3]/div/div[2]/div[1]/div/div/div/div[1]/div/label/div/input") 
buscar_elemento.send_keys("Galaxy Z Flip4 Pink Gold")
time.sleep(1)
buscar_elemento.send_keys(Keys.ENTER)
time.sleep(10)

ingresarElemento = driver.find_element(By.XPATH, '/html/body/div[2]/div/div[1]/div/div[1]/div/div[2]/section/div[2]/div/div/section/div/div[2]/div/div[3]/div/div/div/div[2]/div/section/a/article/div[3]/div/div/img')
ingresarElemento.click()

elegirSCare = driver.find_element(By.XPATH, '//*[@id="WarrantyDetails-2"]')
elegirSCare.click()

terminosycond = driver.find_element(By.ID, 'samsungar-checkbox__care')
terminosycond.click()

comprar = driver.find_element(By.XPATH, '//*[@id="product-button-add-to-cart"]/button')
comprar.click()

#VALIDO QUE el usuario no pueda añadir el producto al carrito si no acepta los "Samsung Care+ Terms and Conditions"
terminos = driver.find_element(By.ID, 'samsungar-checkbox__care') 
camposOb = driver.find_element(By.XPATH, 'samsungar-checkbox__care').text
ExpResult = camposOb

carritoCantidad = driver.find_element(By.XPATH, '//*[@id="headerSamsung"]/div[2]/div/div/div[1]/aside/div/div/button/div/span/span')   
labelCantidad = driver.find_element(By.XPATH, '//*[@id="headerSamsung"]/div[2]/div/div/div[1]/aside/div/div/button/div/span/span').text
ActResult = labelCantidad

def compararSamCare():
    if ActResult == 0:
        print("Los Samsung Care+ Terms and Conditions son un campo obligatorio, debe aceptarlos")
    else:
        print("Se añadió correctamente el producto")
    compararSamCare()

driver.close()


# 
# # popap = driver.find_element(By.XPATH, "/html/body/div[3]/div[1]/div/div/section/div[1]/button")
# popap.click()
# time.sleep(1)

# cookies = driver.find_element(By.ID, 'truste-consent-button')
# cookies.click()
# time.sleep(1)

# login = driver.find_element(By.XPATH, '//*[@id="headerSamsung"]/div[2]/div/div/div[1]/a[2]')
# login.click()
# time.sleep(20)