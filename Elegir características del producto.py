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

login = driver.find_element(By.XPATH, '//*[@id="headerSamsung"]/div[2]/div/div/div[1]/a[2]')
login.click()
time.sleep(20)

usuario = driver.find_element(By.XPATH, "/html/body/div[2]/div/div[1]/div/div[2]/div/div/div/div[2]/div/div/form/div[1]/label/div/input")
usuario.send_keys("gimealvarez2000@gmail.com")
usuario.send_keys(Keys.TAB)
time.sleep(10)

contrasenia = driver.find_element(By.XPATH, "/html/body/div[2]/div/div[1]/div/div[2]/div/div/div/div[2]/div/div/form/div[2]/div/label/div/input")
contrasenia.send_keys("Gimena00")
contrasenia.send_keys(Keys.ENTER)
time.sleep(10)

barra_busqueda = driver.find_element(By.XPATH, "/html/body/div[2]/div/div[1]/div/div[1]/div[2]/div/div/div[1]/a[1]")
barra_busqueda.click()
time.sleep(15)

buscar_producto = driver.find_element(By.XPATH, "/html/body/div[2]/div/div[1]/div/div[1]/div[3]/div/div[2]/div[1]/div/div/div/div[1]/div/label/div/input")
buscar_producto.send_keys("Galaxy Z Flip4 Pink Gold")
time.sleep(5)
buscar_producto.send_keys(Keys.ENTER)
time.sleep(10)

producto = driver.find_element(By.XPATH, '/html/body/div[2]/div/div[1]/div/div[3]/div/div[2]/section/div[2]/div/div/section/div/div[2]/div/div[3]/div/div/div/div[2]/div[1]/section/a/article/div[3]/div/div/img')                         
time.sleep(15)

#VALIDO QUE SI NO HAY STOCK DE UN PRODUCTO CON DETERMINADAS CARACTERISTICAS NO SE AGREGUE AL CARRITO, el carrito estará vacío
noStock = driver.find_element(By.XPATH, '//*[@id="samsungar"]/button')   
labelNoStock = driver.find_element(By.XPATH, '//*[@id="samsungar"]/button').text
ExpResult = labelNoStock

carritoCantidad = driver.find_element(By.XPATH, '//*[@id="headerSamsung"]/div[2]/div/div/div[1]/aside/div/div/button/div/span/span')   
labelCantidad = driver.find_element(By.XPATH, '//*[@id="headerSamsung"]/div[2]/div/div/div[1]/aside/div/div/button/div/span/span').text
ActResult = labelCantidad

def compararStock():
    if ActResult == 0:
        print("No hay stock del producto con las caracteristicas seleccionadas, le avisaremos cuando haya stock")
    else:
        print("Se añadió correctamente el producto")
    compararStock()

caracteristicaSinStock = driver.find_element(By.XPATH, '/html/body/div[2]/div/div[1]/div/div[1]/div/div[2]/section/div[2]/div/div/section/div/div[2]/div/div[3]/div/div/div/div[2]/div[1]/section/a/article/div[5]/div/div[1]/div/div[2]/div[1]/div[1]')
driver.execute_script("window.scrollTo(0,1200)")
time.sleep(10)

driver.close()

# def botonComprar():
#     if ExpResult in ActResult:
#         print("Pass")
#     else:
#         print("Fail")

# comprar = driver.find_element(By.XPATH, '//*[@id="samsungar"]/button')   
# #Aquí identificamos el elemento
# labelComprar = driver.find_element(By.XPATH, '//*[@id="samsungar"]/button').text
# #Aquí extraemos el texto dentro del elemento
# ActResult = labelComprar
# print(ActResult)
# ExpResult = 'Comprar'
# botonComprar()

# caracteristicaConStock = driver.find_element(By.XPATH, '/html/body/div[2]/div/div[1]/div/div/div/div[2]/div/div[7]/div/section/div/div[2]/div/div[3]/div/div[2]/div/div[1]/div')
# driver.execute_script("window.scrollTo(0,1200)")
# time.sleep(10)