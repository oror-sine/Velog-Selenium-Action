from selenium import webdriver
import chromedriver_autoinstaller

chromedriver_autoinstaller.install()

_options = [
    "--headless",
    "--disable-gpu",
    "--window-size=1920,1200",
    "--ignore-certificate-errors",
    "--disable-extensions",
    "--no-sandbox",
    "--disable-dev-shm-usage",
    '--remote-debugging-port=9222'
]

def get_driver(options = _options):
    chrome_options = webdriver.ChromeOptions()
        
    for option in options:
        chrome_options.add_argument(option)

    return webdriver.Chrome(options = chrome_options)

if __name__ == "__main__":
    print(f'{"[Test `get_driver.py`]":-^100}\n')

    print(f'{"[Try Headless]":-^100}')
    status = ''
    try:
        driver_with_headless = get_driver()
        driver_with_headless.get('https://github.com/')
        title = driver_with_headless.title
        driver_with_headless.quit()
        
        status = f'{"Success": <10}: {title}'

    except Exception as err:
        status = f'{"Fail": <10}: {err}'

    print(status)
    print(f'{"":-^100}')


    print(f'{"[Try Display]":-^100}')
    status = ''
    try:
        driver_with_display = get_driver()
        driver_with_display.get('https://github.com/')
        title = driver_with_display.title
        driver_with_display.quit()
        
        status = f'{"Success": <10}: {title}'
        
    except Exception as err:
        status = f'{"Fail": <10}: {err}'

    print(status)
    print(f'{"":-^100}')