# wine_sweet


## Descrição
Web Crawler feito em Python para recuperar vinhos doces da Wine

## Tecnologias utilizadas
- Scrapy
- Pipenv

## Como executar
```
pip install pipenv
pipenv run scrapy crawl Wine --overwrite-output ../output.xml
```
Ao final da execução, será gerado um arquivo output.xml com as urls dos vinhos doces. 