from selenium.webdriver.common.by import By


class MainPageLocators:

    QUESTION_LOCATOR = By.ID, "accordion__heading-{}"
    QUESTION_LOCATOR_FOR_SCROLL = By.ID, "accordion__heading-7"
    ANSWER_LOCATOR = By.XPATH, "//div[@id='accordion__panel-{}']/p"
    UP_BUTTON_ORDER = By.CLASS_NAME, "Button_Button__ra12g"
    DOWN_BUTTON_ORDER = By.XPATH, "//div[@class='Home_FinishButton__1_cWm']"
    SCOOTER_IMAGE = By.XPATH, "//img[@alt='Scooter blueprint']"
    SCOOTER_LOGO = By.XPATH, "//img[@alt='Scooter']"
    YANDEX_LOGO = By.XPATH, "//img[@alt='Yandex']"
