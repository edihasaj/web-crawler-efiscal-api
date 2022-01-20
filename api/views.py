from django.http import HttpResponse
from rest_framework.decorators import api_view
from selenium import webdriver
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.firefox.options import Options


@api_view(["POST"])
def efiscal(request):
    query = request.data['Query']

    options = Options()
    options.headless = True
    browser = webdriver.Firefox(executable_path='C:\geckodriver\geckodriver.exe', options=options)
    browser.get(query)
    delay = 120
    try:
        html_text = WebDriverWait(browser, delay).until(EC.presence_of_element_located((By.CLASS_NAME, 'panel-body')))
        nivf_index = html_text.text.find('NIVF')
        nivf_index = nivf_index + 5
	    

        response = HttpResponse(html_text.text[nivf_index:nivf_index + 37], content_type='text/plain')

        browser.quit()
        
        return response
    except TimeoutException:
        print("Loading took too much time!")
	    
        browser.quit()

    browser.quit()
    return HttpResponse('Kerkimi per nivf morri shume kohe. Provo perseri!', content_type='text/plain')