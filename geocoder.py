from geopy.geocoders import Nominatim


locator = Nominatim()


def geocode(adress):
    return locator.geocode('%s, Hamburg, Deutschland' % str(adress))
