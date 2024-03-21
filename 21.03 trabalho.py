from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

service = Service(executable_path='C:\\Users\\labjf\\Documents\\tdxzin\\chromedriver-win32\\chromedriver.exe')
options = webdriver.ChromeOptions()

driver = webdriver.Chrome(service=service, options=options)
driver.get('https://www.amazon.com.br/?tag=msndesktopabk-20&ref=pd_sl_7to86bd2ph_e&adgrpid=1141293728081284&hvadid=71330944898461&hvnetw=o&hvqmt=e&hvbmt=be&hvdev=c&hvlocint=&hvlocphy=147537&hvtargid=kwd-71331371436168:loc-20&hydadcr=26346_10554304')
try:
    driver.implicitly_wait(2) 
    btn_login = driver.find_element(By.XPATH, '//*[@id="nav-signin-tooltip"]/a/span')
    btn_login.click()
    print("1")

    email_login = driver.find_element(By.ID, 'ap_email')
    email_login.send_keys("parceiroerick@gmail.com")
    print("2")
    
    btn_continuar = driver.find_element(By.XPATH,'//*[@id="continue"]')
    btn_continuar.click()
    print("sucesso1")
    
    
    senha_login = driver.find_element(By.ID, 'ap_password')
    senha_login.send_keys('erick66789')
    print("3")

    btn_fazerlogin = driver.find_element(By.XPATH, '//*[@id="signInSubmit"]')
    btn_fazerlogin.click()
    print("sucesso2")

    campo_busca = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, 'twotabsearchtextbox')))
    print("4")
    campo_busca.send_keys('ventilador')

    print("5")

    btn_ventilador = driver.find_element(By.XPATH, '//*[@id="nav-flyout-searchAjax"]/div[2]/div/div[1]/div[1]/div/div[2]')
    btn_ventilador.click()


    print("sucesso3")
    btn_ventilador = driver.find_element(By.ID, 'a-autoid-3-announce')
    btn_ventilador.click()
    print("sucesso4")
    
    btn_carrinho = driver.find_element(By.ID, 'nav-cart-count')
    btn_carrinho.click()
    print("sucesso5")

except:
    print("Teste Falhou! Não foi possível postar o comentário.")

driver.quit()