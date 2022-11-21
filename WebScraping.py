import requests
from bs4 import BeautifulSoup
import csv

# ------------Modifica los parametros segun tu busqueda------------
'''Indica la url de la página la etiqueta donde se encuentra la información,
el selector id o class y el identificador del selector.'''

url = 'https://supermercado.eroski.es/es/supermercado/2059806-alimentacion/2059988-aceite-vinagre-sal-harina-y-pan-rallado/2059992-aceite-de-girasol'
htmltag = 'div'
htmlselect = 'class'
htmlid = 'product-description'

'''Actualmente solo se admite formato CSV'''

filetype = 'csv'

'''Datos a recuperar: nombre del dato, etiqueta html del dato, class o id, identificador del selector'''

info = [
    ['name', 'h2', 'class', 'product-title product-title-resp'],
    ['price', 'span', 'class', 'price-offer-now']
]


#------------Progam------------

pagedata = [url, htmltag, htmlselect, htmlid]

def get(pagedata, info):
    headers = {"User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.97 Safari/537.36"}
    r = requests.get(pagedata[0], headers=headers)
    soup = BeautifulSoup(r.content, 'html.parser')
    data = []
    if pagedata[2] == "class":
        soup = soup.find_all(pagedata[1], class_= pagedata[3])
        for noodle in soup:
            noodledata = []
            for item in info:
                fact = noodle.find(item[1], {item[2]:item[3]})
                fact = fact.text
                noodledata.append(fact)
            data.append(noodledata)
        while([] in data):
            data.remove([])
        return data
    else:
        soup = soup.find_all(pagedata[1], id_= pagedata[3])
        data = []
        if pagedata[2] == "class":
            soup = soup.find_all(pagedata[1], class_= pagedata[3])
            for noodle in soup:
                noodledata = []
                for item in info:
                    fact = noodle.find(item[1], {item[2]:item[3]})
                    fact = fact.text
                    noodledata.append(fact)
                data.append(noodledata)
        while([] in data):
            data.remove([])
        return data

def reportToFile(info, data, filetype):
    if filetype == 'csv':
        with open('ReportWebScraping.csv', 'w', newline='') as f:
            write = csv.writer(f)
            for item in data:
                print(item)
                write.writerow(item)
    else:
        print('Indica un tipo de archivo para el reporte.')

if __name__ == "__main__":
    data = get(pagedata, info)
    print(data)
    reportToFile(info, data, filetype)
    