import requests
import re

def get_number():
    while 1:
        number = input ('Enter the # from top (1 - 57000): ')
        if re.match(r'\d+$', number) != None:
                if 1<=int(number)<=57000:
                    return int(number)
                else:
                    print ('Please enter a number from 1 to 57000')
        else:
            print ('Not a number')

def get_page_number(number, amount_on_page):
    page_number = (number - 1) // amount_on_page + 1
    return page_number

def get_url (page_number):
    if page_number == 1:
        url = 'http://bash.im/byrating'
    else:
        url = 'http://bash.im/byrating/' + str(page_number)

    return url

def get_quote (request_url, number, amount_on_page):
    content = str(requests.get(request_url).content.decode("cp1251"))
    content = re.findall(r'<div class="text">(.*)</div>', content)
    
    return content[number%50-1].replace('<br>','\n')

amount_on_page = 50

number = get_number()
page_number = get_page_number(number, amount_on_page)
request_url = get_url(page_number)

print(get_quote(request_url, number, amount_on_page))