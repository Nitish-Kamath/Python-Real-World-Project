# URL :Uniform Resource Locator

# URL shortening is a technique on the World Wide Web in which a Uniform Resource Locator (URL) may be made substantially shorter and still direct to the required page. This is achieved by using a redirect which links to the web page that has a long URL. For example, the URL "https://example.com/assets/category_B/subcategory_C/Foo/" can be shortened to "https://example.com/Foo", and the URL "https://en.wikipedia.org/wiki/URL_shortening" can be shortened to "https://w.wiki/U". Often the redirect domain name is shorter than the original one. 

import pyshorteners 

url = input("Enter your Url Here :\n")

print("url after shortening :- ",pyshorteners.Shortener().tinyurl.short(url))