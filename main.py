# main.py
from actions import MumzworldAutomation

if __name__ == "__main__":
    bot = MumzworldAutomation()

    bot.opens_mumzworld_web_store()
    bot.search_a_product("bathing")
    bot.add_products_to_bag()
    bot.go_to_view_bag()
    bot.update_the_qty()
    bot.click_proceed_to_checkout()
    bot.register_a_new_user()
    bot.close_browser()
