from geopy.geocoders import Nominatim


locator = Nominatim()


def geocode(address):
    return locator.geocode('%s, Hamburg, Deutschland' % str(address))
