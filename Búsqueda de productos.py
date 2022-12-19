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
time.sleep(5)

#VALIDO LA BÚSQUEDA DEL PRODUCTO, QUE EL NOMBRE BUSCADO SEA EL ENCONTRADO, contrastando barra de búsqueda y header del producto
busquedaEsperada = driver.find_element(By.XPATH, 'downshift-7-input')   
labelEsperado = driver.find_element(By.XPATH, 'downshift-7-input').text
ExpResult = labelEsperado 

busquedaObtenida = driver.find_element(By.XPATH, '/html/body/div[2]/div/div[1]/div/div[1]/div/div[2]/section/div[2]/div/div/section/div/div[2]/div/div[3]/div/div/div/div[2]/div[1]/section/a/article/h3')   
labelObtenido = driver.find_element(By.XPATH, '/html/body/div[2]/div/div[1]/div/div[1]/div/div[2]/section/div[2]/div/div/section/div/div[2]/div/div[3]/div/div/div/div[2]/div[1]/section/a/article/h3').text
ActResult = labelObtenido  

def validarBusqueda():
    if ExpResult == ActResult:
         print(ActResult)
         print("El producto buscado coincide con el encontrado")
    else:
         print(ActResult)
         print("La búsqueda y el resultado no son coincidenetes")
    validarBusqueda()

buscar_elemento = driver.find_element(By.XPATH, "/html/body/div[2]/div/div[1]/div/div[1]/div[3]/div/div[2]/div[1]/div/div/div/div[1]/div/label/div/input") 
buscar_elemento.send_keys("Galaxy Z Flip4 Pink Gold")
time.sleep(1)
buscar_elemento.send_keys(Keys.ENTER)
time.sleep(10)
            
driver.close()


# def compararLogin():
#     if ExpResult in ActResult:
#         print("Pass")
#     else:
#         print("Fail")

# encabezadoLogin = driver.find_element(By.XPATH, '/html/body/div[2]/div/div[1]/div/div[2]/div/div/div/div[2]/div/div/h3')   
# #Aquí identificamos el elemento
# labelEncabezadoLogin = driver.find_element(By.XPATH, '/html/body/div[2]/div/div[1]/div/div[2]/div/div/div/div[2]/div/div/h3').text
# #Aquí extraemos el texto dentro del elemento
# ActResult = labelEncabezadoLogin #ActResult = actual result = requirement 
# print(ActResult)
# ExpResult = 'Entrar con e-mail y contraseña' #ExpResult = expected result = requirement
# compararLogin()
# producto = driver.find_element(By.XPATH, '/html/body/div[2]/div/div[1]/div/div[3]/div/div[2]/section/div[2]/div/div/section/div/div[2]/div/div[3]/div/div/div/div[2]/div[1]/section/a/article/div[3]/div/div/img')
# producto.click()                          
# time.sleep(15)

# scroll = driver.find_element(By.XPATH, '/html/body/div[2]/div/div[1]/div/div/div/div[2]/div/div[7]/div/section/div/div[2]/div/div[3]/div/div[2]/div/div[2]/div')   
# driver.execute_script("window.scrollTo(0,1200)")
# time.sleep(10)     