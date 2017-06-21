from bs4 import BeautifulSoup
from pprint import pprint

def find_(name):
    with open('data/bencao_detail','r',encoding='utf8') as file:
        list_bencao = file.readlines()
    for line in list_bencao:
        dict_bencao = eval(line)
        if name==dict_bencao['result']['name']:
            return(dict_bencao)
        
def medica_value(name):
    a = find_(name)
    soup = BeautifulSoup(a['result']['content'],"html.parser")
    释名 = soup.find_all('p')[0].get_text()
    气味 = soup.find_all('p')[1].get_text()
    主治 = soup.find_all('p')[2].get_text()
    list_medica = [释名,气味,主治]
    return(list_medica)