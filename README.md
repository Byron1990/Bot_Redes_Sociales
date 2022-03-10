1. Instalar chromedriver

2. Actualizar el PATH

3. Instalar Selenium y crear un ambiente virtual

4. Test:

   1. Abrir el explorador

      ```python
      bot=TinderBot()
      ```

      

5. Identificar elementos:

   1. Buscar elementos para presionar utilizando Selenium, en este caso los buscaremos utilizando XPATH:

      ```python
      bot.driver.find_element_by_xpath('xpath')
      ```

      Para más información en el siguiente enlace:

      https://selenium-python.readthedocs.io/locating-elements.html

6. En el caso de una popup window debemos detectar cual es la nueva ventana con el siguiente comando:

   ```python
   bot.driver.window_handles
   ```

   En segundo identificador es la nueva ventana

7. Regresamos a la ventana principal después de ejecutarse el login

   ```python
   bot.driver.switch_to.window(base_window)
   ```

   

   

