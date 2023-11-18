from gdacs.api import GDACSAPIReader

import json
from os import system, name
from time import sleep


client = GDACSAPIReader()
d={}
c={}


#clear text from console window, depending on os type
def clear_console():
    system('cls' if name=='nt' else 'clear')


#function, responsible for calling other methods for data and displaying it
def display_data():
    events = client.latest_events()
    for entry in sorted(parse_data(str(event)) for event in events):
        print(f'{entry}\n')
    print('Data is updated every 5 minutes.')


#python data parser using json (bad solution)
def parse_data(data : str) -> str:
    global c
    global d
    try:
        d = json.loads(data.replace('\'', '"').replace('None', '"None"'))
        c = d["geo:Point"]
        b = d["gdacs:population"]
        return f'{d["gdacs:country"]} | {d["gdacs:fromdate"]} | {d["title"]} | {d["description"]} | {d["link"]} | coordinates: {c["geo:lat"]}, {c["geo:long"]} | affection: {b["#text"]}'

    except:
        return f'{d["gdacs:country"]} | {d["gdacs:fromdate"]} | {d["title"]} | {d["description"]} | {d["link"]} | coordinates: {c["geo:lat"]}, {c["geo:long"]}'
        

def main():
    try:
        while 1:
            clear_console()
            display_data()
            sleep(300)
            
    except Exception as e:
        print(f'Error: {e} - will retry in 5 minutes.')
        sleep(300)
        main()


if __name__ == '__main__':
    main()
