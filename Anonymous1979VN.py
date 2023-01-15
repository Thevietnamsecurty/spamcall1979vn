#!/usr/bin/env python3
#-*- coding: utf-8 -*-
#By Ma Văn Nam

import requests, re , colorama
colorama.init()
print("""
\033[1;33m\033[1;33m
##     ##    ###     ######  ##    ## #### ##    ##  ######         ##    #######  ########  #######     ##     ## ##    ##    ##     ##    ##   
##     ##   ## ##   ##    ## ##   ##   ##  ###   ## ##    ##      ####   ##     ## ##    ## ##     ##    ##     ## ###   ##    ##     ##  ####   
##     ##  ##   ##  ##       ##  ##    ##  ####  ## ##              ##   ##     ##     ##   ##     ##    ##     ## ####  ##    ##     ##    ##   
######### ##     ## ##       #####     ##  ## ## ## ##   ####       ##    ########    ##     ########    ##     ## ## ## ##    ##     ##    ##   
##     ## ######### ##       ##  ##    ##  ##  #### ##    ##        ##          ##   ##            ##     ##   ##  ##  ####     ##   ##     ##   
##     ## ##     ## ##    ## ##   ##   ##  ##   ### ##    ##        ##   ##     ##   ##     ##     ##      ## ##   ##   ###      ## ##      ##   
##     ## ##     ##  ######  ##    ## #### ##    ##  ######       ######  #######    ##      #######        ###    ##    ##       ###     ###### 
""")

try:
    print()
    countries = ["US", "JP", "IT", "KR", "FR", "DE", "TW", "RU", "GB", "NL",
                 "CZ", "TR", "AT", "CH", "ES", "CA", "SE", "IL", "PL", "IR",
                 "NO", "RO", "IN", "VN", "BE", "BR", "BG", "ID", "DK", "AR",
                 "MX", "FI", "CN", "CL", "ZA", "SK", "HU", "IE", "EG", "TH",
                 "UA", "RS", "HK", "GR", "PT", "LV", "SG", "IS", "MY", "CO",
                 "TN", "EE", "DO", "SI", "EC", "LT", "PS", "NZ", "BD", "PA",
                 "MD", "NI", "MT", "TT", "SA", "HR", "CY", "PK", "AE", "KZ",
                 "KW", "VE", "GE", "ME", "SV", "LU", "CW", "PR", "CR", "BY",
                 "AL", "LI", "BA", "PY", "PH", "FO", "GT", "NP", "PE", "UY",
                 "-" , "AD", "AG", "AM", "AO", "AU", "AW", "AZ", "BB", 
                 "BQ", "BS", "BW", "CG", "CI", "DZ", "FJ", "GA", "GG", "GL",
                 "GP", "GU", "GY", "HN", "JE", "JM", "JO", "KE", "KH", "KN",
                 "KY", "LA", "LB", "LK", "MA", "MG", "MK", "MN", "MO", "MQ",
                 "MU", "NA", "NC", "NG", "QA", "RE", "SD", "SN", "SR", "ST",
                 "SY", "TZ", "UG", "UZ", "VC","BJ", ]
    headers = {"User-Agent": "Mozilla/5.0 (X11; Linux i686; rv:68.0) Gecko/20100101 Firefox/68.0"}

    num = int(input("@MAVANNAM ---> "))
    if num not in range(1, 145+1):
        raise IndexError

    country = countries[num-1]
    res = requests.get(
        f"http://www.insecam.org/en/bycountry/{country}", headers=headers
    )
    last_page = re.findall(r'pagenavigator\("\?page=", (\d+)', res.text)[0]

    for page in range(int(last_page)):
        res = requests.get(
            f"http://www.insecam.org/en/bycountry/{country}/?page={page}",
            headers=headers
        )
        find_ip = re.findall(r"http://\d+.\d+.\d+.\d+:\d+", res.text)
        for ip in find_ip:
            print("\033[1;34m", ip)
except:
    pass
finally:
    print("\033[1;34m")
    exit()
