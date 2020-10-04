import geoip2.database
reader = geoip2.database.Reader('./GeoLite2-City.mmdb')
ip="67.240.52.23"
data=reader.city(ip)
print(data.city.name)