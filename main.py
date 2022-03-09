import requests
from pyfiglet import Figlet
import folium
from termcolor import colored, cprint
import colorama
from colorama import Fore, Back, Style
colorama.init()


def get_info_ip(ip='127.0.0.1'):
    try:
        response = requests.get(url=f'http://ip-api.com/json/{ip}').json()

        data = {
            '[IP]': response.get('query'),
            '[Internet provider]': response.get('isp'),
            '[Organization]': response.get('org'),
            '[Country]': response.get('country'),
            '[Region name]': response.get('regionName'),
            '[City]': response.get('city'),
            '[Zip code]': response.get('zip'),
            '[Width]': response.get('lat'),
            '[Longitude]': response.get('lon'),
        }

        for i, x in data.items():
            print(f'{i} : {x}')

        mapping = folium.Map(location=[response.get('lat'), response.get('lon')])
        mapping.save(f'{response.get("query")}_{response.get("city")}.html')

    except requests.exceptions.ConnectionError:
        print(colored('{!} Please check your connection!', 'red', attrs=['underline']))
    except TypeError:
        print(colored('{!} Invalid IP address. Example: 192.168.0.20', 'red', attrs=['underline']))
        exit()
    except ValueError:
        print(colored('{!} Invalid IP address. Example: 192.168.0.20', 'red', attrs=['underline']))
        exit()


def main():
    preview_text = Figlet(font='cyberlarge')
    preview_author = Figlet(font='slant')
    print(preview_text.renderText('IP INFO'))
    ip = input(colored('Please enter a target IP: ', 'red', attrs=['underline']))
    get_info_ip(ip=ip)
    print(preview_author.renderText('BY CODE0EYES'))


if __name__ == '__main__':
    main()