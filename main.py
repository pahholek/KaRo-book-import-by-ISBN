def get_data(isbn):
    import requests
    from bs4 import BeautifulSoup
    isbn = str(isbn)

    payload = {
        'kl':'',
        'al': '',
        'priority':'1',
        'uid':'',
        'dist':'2',
        'lok':'all',
        'liczba':'5',
        'pubyearh':'',
        'pubyearl':'',
        'lang':'pl',
        'bib':'UJ',
        'si':'1',
        'qt':'F',
        'di':'i'+isbn,
        'pp':'1',
        'detail':'3',
        'pm':'m',
        'st1':'ie'+isbn,
    }

    r = requests.get('https://karo.umk.pl/K_3.02/Exec/z2w_f.pl', params=payload)
    html = r.text
    print(r.url)
    from bs4 import BeautifulSoup

    soup = BeautifulSoup(html, 'lxml')
    html_data = soup.find('table', {'class': 'fulltbl'})
    table_data = [[cell.text for cell in row("td")]
                  for row in soup("tr")]
    table_size = len(table_data)
    table_data_clean = []
    #junk off
    for i in range(table_size):
        try:
            int(table_data[i][0])
            table_data_clean.append(table_data[i])
        except:
            print('data in cleaning')

    print(table_data_clean)


    #check if data is present
    table_data_trimmed = []
    if table_data_clean == []:
        return 'No_Data'
    else:
        for i in range(table_size):
            if int(table_data_clean[i][0]) == 245:
                table_data_trimmed.append(table_data_clean[i])
            if int(table_data_clean[i][0]) == 260:
                table_data_trimmed.append(table_data_clean[i])
            if int(table_data_clean[i][0]) == 700:
                table_data.append(table_data_clean[i])


print(get_data(9788381181341))
