# OTUS Web homework 2
> Simple site parser

This script allows you to parse some site articles and show words frequency 
statistic.

## Installation

```bash
$ pip install requirements.txt
```

## Run
```bash
$ python app.py -s https://habr.com/all/
```

## Results
```
2018-05-10 - 2018-05-07
компания: 36
год: 30
система: 29
статья: 28
работа: 27
информация: 24
код: 23
тестирование: 23
часть: 22
разработка: 20
```

### Command line arguments

- `-s`, site address. *Required*.
- `--p`, page number. Default `10`.
- `--t`, number of top words. Default `10`.
- `--pag'`, how pagination look like. Default `page{}/`.
- `--tc`, article's title CSS class. Default `post__title_link'`.
- `--ac`, article's article CSS class. Default `post__text`.
- `--ab`, article's article block CSS class. Default `post post_preview`.
- `--tb`, article's date block CSS class. Default `post__time`.