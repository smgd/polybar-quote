# polybar-quote
Random quote script for [Polybar](https://github.com/jaagr/polybar). Thanks http://forismatic.com for API.
![preview](https://github.com/soapmangoesdown/polybar-random-quote/raw/master/preview.png)

### Module
```ini
[module/quote]
type = custom/script
exec = ~/.config/polybar/random-quote/quote.py
click-left = python ~/.config/polybar/random-quote/goo.py
interval = 60
```
### Script arguments
`-l` or `--lang` - to change quote language ('ru' or 'en'), default: 'en'
`-s` or `--size` - to change the maximum length (in symbols) of the quote, default: '150'
#### Example
```ini
[module/quote]
type = custom/script
exec = ~/.config/polybar/random-quote/quote.py --lang='ru'
click-left = python ~/.config/polybar/random-quote/goo.py
interval = 60
```
