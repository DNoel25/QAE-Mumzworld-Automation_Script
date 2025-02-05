class Locators:
    POPUP_HOST = "#wzrkImageOnlyDiv > ct-web-popup-imageonly"
    POPUP_CLOSE = "#close"

    LOGO = "//a[@id='mumz_logo_img']"
    SEARCH_BAR = '//*[@id="search_textbox"]'
    SEARCH_RESULTS = ".ais-InfiniteHits-list"

    ADD_TO_CART_BUTTON = "(//button[@id='add_cart_button'])[1]"
    CART_BUTTON = "//a[@id='cart_button' and contains(@title, 'Cart')]"

    QTY_INPUT = "//input[@name='qty' and @type='number' and contains(@class, 'text-lg')]"
    PROCEED_CHECKOUT_BUTTON = "//button[@title='Proceed to Checkout']"

    NAV_CREATE_ACCOUNT = "//a[@id='create_account_button']"