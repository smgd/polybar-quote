# polybar-quote
Random quote script for [Polybar](https://github.com/jaagr/polybar). Thanks http://forismatic.com for API.
![preview](https://github.com/soapmangoesdown/polybar-random-quote/raw/master/preview.png)

## Dependencies
```sh
sudo pip install requests
```
## Installation
```sh
cd ~/.config/polybar
curl -LO https://github.com/soapmangoesdown/polybar-quote/archive/master.tar.gz
tar zxf master.tar.gz && rm master.tar.gz
mv polybar-quote-master random-quote
```

## Module
```ini
[module/quote]
type = custom/script
exec = ~/.config/polybar/random-quote/quote.py
click-left = python ~/.config/polybar/random-quote/goo.py
interval = 60
```
### Script arguments
`-l` or `--lang` - to change quote language ('ru' or 'en'), default: 'en'
`-s` or `--size` - to change the maximum length of the quote, default: '150'
#### Example
```ini
[module/quote]
type = custom/script
exec = ~/.config/polybar/random-quote/quote.py --lang='ru'
click-left = python ~/.config/polybar/random-quote/goo.py
interval = 60
```
