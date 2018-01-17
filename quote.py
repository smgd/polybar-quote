#!/usr/bin/env python3

import requests

r = requests.get("https://api.forismatic.com/api/1.0/?method=getQuote&lang=en&format=text")
quote = r.text.replace('  ', ' ').replace(' )', ')').replace('  ', ' ').strip()
print(quote)
