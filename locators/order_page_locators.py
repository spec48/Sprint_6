from selenium.webdriver.common.by import By


class OrderPageLocators:

    FIELD_NAME = By.XPATH, "//input[@placeholder='* Имя']"
    FIELD_LAST_NAME = By.XPATH, "//input[@placeholder='* Фамилия']"
    FIELD_ADDRESS = By.XPATH, "//input[@placeholder='* Адрес: куда привезти заказ']"
    FIELD_METRO = By.XPATH, "//input[@placeholder='* Станция метро']"
    METRO = By.XPATH, "//div[@class='Order_Text__2broi' and text()='{}']"
    FIELD_PHONE = By.XPATH, "//input[@placeholder='* Телефон: на него позвонит курьер']"
    BUTTON_NEXT = By.XPATH, "//button[text()='Далее']"
    FIELD_DELIVERY_DATE = By.XPATH, "//input[@placeholder='* Когда привезти самокат']"
    FIELD_RENTAL_PERIOD = By.XPATH, "//div[@class='Dropdown-placeholder']"
    RENTA_PERIOD = By.XPATH, "//div[@class='Dropdown-option' and text()='{}']"
    COLOR = By.XPATH, "//input[@id='{}']"
    COMMENT = By.XPATH, "//input[@placeholder='Комментарий для курьера']"
    ORDER_BUTTON = By.XPATH, "//button[@class='Button_Button__ra12g Button_Middle__1CSJM']"
    POPUP_WINDOW = By.XPATH, "//div[@class='Order_Text__2broi']"
