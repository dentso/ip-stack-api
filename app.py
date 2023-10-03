#!/usr/bin/env python3


import os
import sys
import requests
import argparse
import json

url = 'http://api.ipstack.com/'

if __name__ == "__main__":
    access_key = os.getenv('API_KEY')

    parser = argparse.ArgumentParser(
                    description='Get info from IpStack')
    parser.add_argument('--ip', required=True)
    args = parser.parse_args()
    ip_addr = args.ip

    headers = { 'Accept': 'application/json' }
    r = requests.get(f'{url}/{ip_addr}?access_key={access_key}', headers=headers)
    data = r.json()
    try:
        d = {
                "latt": data["latitude"],
                "long": data["longitude"],
            }
        print(json.dumps(d, indent=2))
        sys.exit(0)
    except KeyError:
        print("ERROR: unable to retrieve the longitude and latitude.")
        sys.exit(1)
