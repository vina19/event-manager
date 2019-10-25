from weather import getWeather
from restaurant_api import getRestaurants
from event_api import getEvents
def main():

    show_menu()

def show_menu():
    print("****Travel App****\n"
              "Enter a city and country code to see"
              " the weather, top restaurants\n and concerts")
    print("You can find country codes at https://en.wikipedia.org/wiki/List_of_ISO_3166_country_codes ")
    city, country_code, keyword = getInput()
    getWeather(city, country_code)
    getRestaurants(city)
    getEvents(city, keyword)




def getInput():
    city = input(("City: "))
    country_code = input(("Country Code: "))
    keyword = input(("Enter keyword for event: "))
    return city, country_code, keyword
    # receiving user input












if __name__ == '__main__':
        main()
