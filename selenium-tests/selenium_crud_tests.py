import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


os.makedirs("capturas", exist_ok=True)

driver = webdriver.Chrome()
driver.get("http://localhost/tarea4/")
driver.save_screenshot("capturas/01_inicio.png")

WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.LINK_TEXT, "Agregar Usuario"))
).click()
time.sleep(1)
driver.find_element(By.NAME, "nombre").send_keys("kelyn tejada")
driver.find_element(By.NAME, "correo").send_keys("tejada01@gmail.com")
driver.find_element(By.NAME, "edad").send_keys("35")
driver.find_element(By.TAG_NAME, "form").submit()
time.sleep(2)
driver.save_screenshot("capturas/02_usuario_creado.png")

assert "kelyn tejada" in driver.page_source
print("Usuario creado correctamente")

driver.find_element(By.LINK_TEXT, "Editar").click()
time.sleep(1)
nombre_input = driver.find_element(By.NAME, "nombre")
nombre_input.clear()
nombre_input.send_keys("kelyn Editado")
driver.find_element(By.TAG_NAME, "form").submit()
time.sleep(2)
driver.save_screenshot("capturas/03_usuario_editado.png")
assert "kelyn Editado" in driver.page_source
print("Usuario editado correctamente")

driver.find_element(By.LINK_TEXT, "Eliminar").click()
time.sleep(1)
alert = driver.switch_to.alert
alert.accept()
time.sleep(2)
driver.save_screenshot("capturas/04_usuario_eliminado.png")
assert "kelyn Editado" not in driver.page_source
print("Usuario eliminado correctamente")
      
driver.find_element(By.LINK_TEXT, "Agregar Usuario").click()
time.sleep(1)
driver.find_element(By.NAME, "nombre").send_keys("")
driver.find_element(By.NAME, "correo").send_keys("")
driver.find_element(By.NAME, "edad").send_keys("")
driver.find_element(By.TAG_NAME, "form").submit()
time.sleep(2)
driver.save_screenshot("capturas/05_error_formulario_vacio.png")

print("Prueba negativa completada (no se debe registrar con campos vacíos)")

driver.quit()
print("Todas las pruebas pasaron exitosamente.")


