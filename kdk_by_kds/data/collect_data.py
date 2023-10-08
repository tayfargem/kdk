# Importing the required libraries
import requests
import pandas as pd
from bs4 import BeautifulSoup

html_table = """ <table id="data-table-default" class="table table-product table-striped display responsive dataTable no-footer dtr-inline" style="width: 100%;" role="grid" aria-describedby="data-table-default_info">
                <thead style="background-color: #cf993d91;">
                    <tr role="row"><th style="width: 64px;" data-type="sikayet-no" class="sorting_desc" tabindex="0" aria-controls="data-table-default" rowspan="1" colspan="1" aria-sort="descending" aria-label="Başvuru No: activate to sort column ascending">Başvuru No</th><th style="width: 62px;" class="sorting" tabindex="0" aria-controls="data-table-default" rowspan="1" colspan="1" aria-label="Karar Tarihi: activate to sort column ascending">Karar Tarihi</th><th style="width:90px;" class="sorting" tabindex="0" aria-controls="data-table-default" rowspan="1" colspan="1" aria-label="Karar Türü: activate to sort column ascending">Karar Türü</th><th class="sorting" tabindex="0" aria-controls="data-table-default" rowspan="1" colspan="1" aria-label="Karar Konusu: activate to sort column ascending" style="width: 344px;">Karar Konusu</th><th class="sorting" tabindex="0" aria-controls="data-table-default" rowspan="1" colspan="1" aria-label="Başvuru Konu İdare: activate to sort column ascending" style="width: 331px;">Başvuru Konu İdare</th><th style="text-align: center;width:90px;" class="sorting" tabindex="0" aria-controls="data-table-default" rowspan="1" colspan="1" aria-label="İşlem: activate to sort column ascending">İşlem</th></tr>
                </thead>
            <tbody><tr role="row" class="odd"><td class="sorting_1" tabindex="0">2023/14080</td>
            <td>19/09/2023</td><td>Ret Kararı</td><td>B sınıfı iş güvenliği uzmanlığı belgesinin verilmesi talebi hakkındadır.</td>
            <td>ÇALIŞMA VE SOSYAL GÜVENLİK BAKANLIĞI</td><td><a class="m-r-20" style="cursor:pointer;" onclick="Detail(1171027)" title="Görüntüle" data-original-title="Görüntüle" data-toggle="modal" data-target="#myModal"><i class="fa fa-sticky-note fa-2x text-primary"></i></a><a href="/Arama/Download?url=20230903\242231\Yayin\Karar-2023-14080.pdf&amp;tarih=2023-09-19T19:23:51.056968" title="İndir" data-original-title="İndir" target="_blank"> <i class="fa fa-download fa-2x text-primary"></i> </a></td></tr><tr role="row" class="even"><td class="sorting_1" tabindex="0">2023/11304</td><td>26/09/2023</td><td>Ret Kararı</td><td>Engellilik mazeretine dayalı nakil talebi hakkındadır.</td><td>MİLLİ EĞİTİM BAKANLIĞI</td><td><a class="m-r-20" style="cursor:pointer;" onclick="Detail(1171171)" title="Görüntüle" data-original-title="Görüntüle" data-toggle="modal" data-target="#myModal"><i class="fa fa-sticky-note fa-2x text-primary"></i></a><a href="/Arama/Download?url=20230801\239455\Yayin\Karar-2023-11304.pdf&amp;tarih=2023-09-26T11:25:08.837383" title="İndir" data-original-title="İndir" target="_blank"> <i class="fa fa-download fa-2x text-primary"></i> </a></td></tr><tr role="row" class="odd"><td class="sorting_1" tabindex="0">2023/11243</td><td>31/08/2023</td><td>Ret Kararı</td><td>Aile birliği mazeretine dayalı görevlendirme ya da nakil talebi hakkındadır.</td><td>SAĞLIK BAKANLIĞI</td><td><a class="m-r-20" style="cursor:pointer;" onclick="Detail(1162701)" title="Görüntüle" data-original-title="Görüntüle" data-toggle="modal" data-target="#myModal"><i class="fa fa-sticky-note fa-2x text-primary"></i></a><a href="/Arama/Download?url=20230730\239394\Yayin\Karar-2023-11243.pdf&amp;tarih=2023-08-31T17:30:44.197606" title="İndir" data-original-title="İndir" target="_blank"> <i class="fa fa-download fa-2x text-primary"></i> </a></td></tr><tr role="row" class="even"><td class="sorting_1" tabindex="0">2023/10562</td><td>31/08/2023</td><td>Kısmen Tavsiye Kısmen Ret Kararı</td><td>Başvuranın Doçentlik unvan şartına bağlı olan özlük haklarından yararlanma talebi hk.</td><td>AMASYA ÜNİVERSİTESİ REKTÖRLÜĞÜ, TÜRKİYE BÜYÜK MİLLET MECLİSİ BAŞKANLIĞI, YÜKSEKÖĞRETİM KURULU BAŞKANLIĞI</td><td><a class="m-r-20" style="cursor:pointer;" onclick="Detail(1163202)" title="Görüntüle" data-original-title="Görüntüle" data-toggle="modal" data-target="#myModal"><i class="fa fa-sticky-note fa-2x text-primary"></i></a><a href="/Arama/Download?url=20230717\238712\Yayin\Karar-2023-10562.pdf&amp;tarih=2023-08-31T17:30:49.134874" title="İndir" data-original-title="İndir" target="_blank"> <i class="fa fa-download fa-2x text-primary"></i> </a></td></tr><tr role="row" class="odd"><td class="sorting_1" tabindex="0">2023/9434</td><td>18/08/2023</td><td>Tavsiye Kararı</td><td>Başvuranın nakil talebi hakkındadır.</td><td>SAĞLIK BAKANLIĞI</td><td><a class="m-r-20" style="cursor:pointer;" onclick="Detail(1157322)" title="Görüntüle" data-original-title="Görüntüle" data-toggle="modal" data-target="#myModal"><i class="fa fa-sticky-note fa-2x text-primary"></i></a><a href="/Arama/Download?url=20230706\237584\Yayin\Karar-2023-9434.pdf&amp;tarih=2023-08-18T16:36:53.492533" title="İndir" data-original-title="İndir" target="_blank"> <i class="fa fa-download fa-2x text-primary"></i> </a></td></tr><tr role="row" class="even"><td class="sorting_1" tabindex="0">2023/9266</td><td>31/08/2023</td><td>Ret Kararı</td><td>Başvuranın Elazığ iline becayiş talebi hakkındadır.</td><td>MİLLİ EĞİTİM BAKANLIĞI</td><td><a class="m-r-20" style="cursor:pointer;" onclick="Detail(1162700)" title="Görüntüle" data-original-title="Görüntüle" data-toggle="modal" data-target="#myModal"><i class="fa fa-sticky-note fa-2x text-primary"></i></a><a href="/Arama/Download?url=20230703\237416\Yayin\Karar-2023-9266.pdf&amp;tarih=2023-08-31T17:30:44.823458" title="İndir" data-original-title="İndir" target="_blank"> <i class="fa fa-download fa-2x text-primary"></i> </a></td></tr><tr role="row" class="odd"><td class="sorting_1" tabindex="0">2023/9161</td><td>19/09/2023</td><td>Ret Kararı</td><td>Soyadı değişikliği yapan başvuranın söz konusu değişiklikten önce aldığı diplomasının yeni soyadıyla yeniden düzenlenmesi talebi hakkındadır.</td><td>ANADOLU ÜNİVERSİTESİ REKTÖRLÜĞÜ</td><td><a class="m-r-20" style="cursor:pointer;" onclick="Detail(1169459)" title="Görüntüle" data-original-title="Görüntüle" data-toggle="modal" data-target="#myModal"><i class="fa fa-sticky-note fa-2x text-primary"></i></a><a href="/Arama/Download?url=20230629\237311\Yayin\Karar-2023-9161.pdf&amp;tarih=2023-09-19T09:51:09.876195" title="İndir" data-original-title="İndir" target="_blank"> <i class="fa fa-download fa-2x text-primary"></i> </a></td></tr><tr role="row" class="even"><td class="sorting_1" tabindex="0">2023/8848</td><td>26/07/2023</td><td>Tavsiye Kararı</td><td>Başvuranın, ücretli öğretmenlik yaptığı dönemlere ilişkin SGK primlerimin tam süreli çalışmaya göre hesaplanarak bildirilmesi talebi hakkındadır.</td><td>MİLLİ EĞİTİM BAKANLIĞI, SOSYAL GÜVENLİK KURUMU BAŞKANLIĞI</td><td><a class="m-r-20" style="cursor:pointer;" onclick="Detail(1146497)" title="Görüntüle" data-original-title="Görüntüle" data-toggle="modal" data-target="#myModal"><i class="fa fa-sticky-note fa-2x text-primary"></i></a><a href="/Arama/Download?url=20230620\236998\Yayin\Karar-2023-8848.pdf&amp;tarih=2023-07-26T10:56:49.426576" title="İndir" data-original-title="İndir" target="_blank"> <i class="fa fa-download fa-2x text-primary"></i> </a></td></tr><tr role="row" class="odd"><td class="sorting_1" tabindex="0">2023/8812</td><td>14/09/2023</td><td>Ret Kararı</td><td>Nakdi yemek yardımı talebi hakkındadır.</td><td>SİMAV BELEDİYE BAŞKANLIĞI</td><td><a class="m-r-20" style="cursor:pointer;" onclick="Detail(1166951)" title="Görüntüle" data-original-title="Görüntüle" data-toggle="modal" data-target="#myModal"><i class="fa fa-sticky-note fa-2x text-primary"></i></a><a href="/Arama/Download?url=20230619\236962\Yayin\Karar-2023-8812.pdf&amp;tarih=2023-09-14T12:25:44.401759" title="İndir" data-original-title="İndir" target="_blank"> <i class="fa fa-download fa-2x text-primary"></i> </a></td></tr><tr role="row" class="even"><td class="sorting_1" tabindex="0">2023/8633</td><td>18/08/2023</td> """


soup = BeautifulSoup(html_table, 'html.parser')

# Find the table element
table = soup.find('table')

# Extract headers (column names)
headers = [header.text.strip() for header in table.find_all('th')]

# Extract rows
rows = []
for row in table.find_all('tr'):
    rows.append([col.text.strip() for col in row.find_all(['td', 'th'])])

# Create a DataFrame
df = pd.DataFrame(rows[1:], columns=headers)

# Display the DataFrame
print(df)

"""
"""
base_url = 'https://kararlar.ombudsman.gov.tr/Arama/Index'
# https://stackoverflow.com/a/71257828
headers = {'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.102 Safari/537.36"}
# HTTP/1.1 200 OK
# Server: nginx
# Date: Sun, 08 Oct 2023 15:20:07 GMT
# Content-Type: text/html; charset=utf-8
# Transfer-Encoding: chunked
# Connection: keep-alive
# Set-Cookie: .AspNetCore.Mvc.CookieTempDataProvider=; expires=Thu, 01 Jan 1970 00:00:00 GMT; path=/; samesite=strict
# Content-Encoding: gzip

# with requests.Session() as s:
s = requests.Session()
r = s.get(base_url, headers=headers)

soup = BeautifulSoup(r.content, 'html.parser')
hidden = soup.find_all("input", {'type': 'hidden'})

payload ='draw=1&columns%5B0%5D%5Bdata%5D=sikayeT_NO&columns%5B0%5D%5Bname%5D=&columns%5B0%5D%5Bsearchable%5D=true&columns%5B0%5D%5Borderable%5D=true&columns%5B0%5D%5Bsearch%5D%5Bvalue%5D=&columns%5B0%5D%5Bsearch%5D%5Bregex%5D=false&columns%5B1%5D%5Bdata%5D=karaR_TARIH&columns%5B1%5D%5Bname%5D=&columns%5B1%5D%5Bsearchable%5D=true&columns%5B1%5D%5Borderable%5D=true&columns%5B1%5D%5Bsearch%5D%5Bvalue%5D=&columns%5B1%5D%5Bsearch%5D%5Bregex%5D=false&columns%5B2%5D%5Bdata%5D=karaR_TURU&columns%5B2%5D%5Bname%5D=&columns%5B2%5D%5Bsearchable%5D=true&columns%5B2%5D%5Borderable%5D=true&columns%5B2%5D%5Bsearch%5D%5Bvalue%5D=&columns%5B2%5D%5Bsearch%5D%5Bregex%5D=false&columns%5B3%5D%5Bdata%5D=evraK_KONU&columns%5B3%5D%5Bname%5D=&columns%5B3%5D%5Bsearchable%5D=true&columns%5B3%5D%5Borderable%5D=true&columns%5B3%5D%5Bsearch%5D%5Bvalue%5D=&columns%5B3%5D%5Bsearch%5D%5Bregex%5D=false&columns%5B4%5D%5Bdata%5D=sikayeT_EDILEN_KURUM&columns%5B4%5D%5Bname%5D=&columns%5B4%5D%5Bsearchable%5D=true&columns%5B4%5D%5Borderable%5D=true&columns%5B4%5D%5Bsearch%5D%5Bvalue%5D=&columns%5B4%5D%5Bsearch%5D%5Bregex%5D=false&columns%5B5%5D%5Bdata%5D=evraK_ID&columns%5B5%5D%5Bname%5D=&columns%5B5%5D%5Bsearchable%5D=true&columns%5B5%5D%5Borderable%5D=true&columns%5B5%5D%5Bsearch%5D%5Bvalue%5D=&columns%5B5%5D%5Bsearch%5D%5Bregex%5D=false&order%5B0%5D%5Bcolumn%5D=0&order%5B0%5D%5Bdir%5D=desc&start=40&length=10&search%5Bvalue%5D=&search%5Bregex%5D=false&basbas=&basbit=&basnoyil=&basnosayi=&sikayetkonu=&konuidarekelimeleri=&karbas=&karbit=&kararTuru=&evrakkonu=&ortakalankelimeleri='

r = s.post('https://kararlar.ombudsman.gov.tr/Arama/IndexPaging', headers=headers, params=payload)
soup = BeautifulSoup(r.content, 'html.parser')

print(soup.title.text)



# draw=3&columns%5B0%5D%5Bdata%5D=sikayeT_NO&columns%5B0%5D%5Bname%5D=&columns%5B0%5D%5Bsearchable%5D=true&columns%5B0%5D%5Borderable%5D=true&columns%5B0%5D%5Bsearch%5D%5Bvalue%5D=&columns%5B0%5D%5Bsearch%5D%5Bregex%5D=false&columns%5B1%5D%5Bdata%5D=karaR_TARIH&columns%5B1%5D%5Bname%5D=&columns%5B1%5D%5Bsearchable%5D=true&columns%5B1%5D%5Borderable%5D=true&columns%5B1%5D%5Bsearch%5D%5Bvalue%5D=&columns%5B1%5D%5Bsearch%5D%5Bregex%5D=false&columns%5B2%5D%5Bdata%5D=karaR_TURU&columns%5B2%5D%5Bname%5D=&columns%5B2%5D%5Bsearchable%5D=true&columns%5B2%5D%5Borderable%5D=true&columns%5B2%5D%5Bsearch%5D%5Bvalue%5D=&columns%5B2%5D%5Bsearch%5D%5Bregex%5D=false&columns%5B3%5D%5Bdata%5D=evraK_KONU&columns%5B3%5D%5Bname%5D=&columns%5B3%5D%5Bsearchable%5D=true&columns%5B3%5D%5Borderable%5D=true&columns%5B3%5D%5Bsearch%5D%5Bvalue%5D=&columns%5B3%5D%5Bsearch%5D%5Bregex%5D=false&columns%5B4%5D%5Bdata%5D=sikayeT_EDILEN_KURUM&columns%5B4%5D%5Bname%5D=&columns%5B4%5D%5Bsearchable%5D=true&columns%5B4%5D%5Borderable%5D=true&columns%5B4%5D%5Bsearch%5D%5Bvalue%5D=&columns%5B4%5D%5Bsearch%5D%5Bregex%5D=false&columns%5B5%5D%5Bdata%5D=evraK_ID&columns%5B5%5D%5Bname%5D=&columns%5B5%5D%5Bsearchable%5D=true&columns%5B5%5D%5Borderable%5D=true&columns%5B5%5D%5Bsearch%5D%5Bvalue%5D=&columns%5B5%5D%5Bsearch%5D%5Bregex%5D=false&order%5B0%5D%5Bcolumn%5D=0&order%5B0%5D%5Bdir%5D=desc&start=20&length=10&search%5Bvalue%5D=&search%5Bregex%5D=false&basbas=&basbit=&basnoyil=&basnosayi=&sikayetkonu=&konuidarekelimeleri=&karbas=&karbit=&kararTuru=&evrakkonu=&ortakalankelimeleri=
# get_page = 3&columns%5B0%5D%5Bdata%5D=sikayeT_NO&columns%5B0%5D%5Bname%5D=&columns%5B0%5D%5Bsearchable%5D=true&columns%5B0%5D%5Borderable%5D=true&columns%5B0%5D%5Bsearch%5D%5Bvalue%5D=&columns%5B0%5D%5Bsearch%5D%5Bregex%5D=false&columns%5B1%5D%5Bdata%5D=karaR_TARIH&columns%5B1%5D%5Bname%5D=&columns%5B1%5D%5Bsearchable%5D=true&columns%5B1%5D%5Borderable%5D=true&columns%5B1%5D%5Bsearch%5D%5Bvalue%5D=&columns%5B1%5D%5Bsearch%5D%5Bregex%5D=false&columns%5B2%5D%5Bdata%5D=karaR_TURU&columns%5B2%5D%5Bname%5D=&columns%5B2%5D%5Bsearchable%5D=true&columns%5B2%5D%5Borderable%5D=true&columns%5B2%5D%5Bsearch%5D%5Bvalue%5D=&columns%5B2%5D%5Bsearch%5D%5Bregex%5D=false&columns%5B3%5D%5Bdata%5D=evraK_KONU&columns%5B3%5D%5Bname%5D=&columns%5B3%5D%5Bsearchable%5D=true&columns%5B3%5D%5Borderable%5D=true&columns%5B3%5D%5Bsearch%5D%5Bvalue%5D=&columns%5B3%5D%5Bsearch%5D%5Bregex%5D=false&columns%5B4%5D%5Bdata%5D=sikayeT_EDILEN_KURUM&columns%5B4%5D%5Bname%5D=&columns%5B4%5D%5Bsearchable%5D=true&columns%5B4%5D%5Borderable%5D=true&columns%5B4%5D%5Bsearch%5D%5Bvalue%5D=&columns%5B4%5D%5Bsearch%5D%5Bregex%5D=false&columns%5B5%5D%5Bdata%5D=evraK_ID&columns%5B5%5D%5Bname%5D=&columns%5B5%5D%5Bsearchable%5D=true&columns%5B5%5D%5Borderable%5D=true&columns%5B5%5D%5Bsearch%5D%5Bvalue%5D=&columns%5B5%5D%5Bsearch%5D%5Bregex%5D=false&order%5B0%5D%5Bcolumn%5D=0&order%5B0%5D%5Bdir%5D=desc&start=20&length=10&search%5Bvalue%5D=&search%5Bregex%5D=false&basbas=&basbit=&basnoyil=&basnosayi=&sikayetkonu=&konuidarekelimeleri=&karbas=&karbit=&kararTuru=&evrakkonu=&ortakalankelimeleri=

data = requests.post(get_page).text

# Downloading contents of the web page
url = "https://kararlar.ombudsman.gov.tr/Arama/Index"
data = requests.get(url).text

#  Creating BeautifulSoup object
soup = BeautifulSoup(data, 'html.parser')

table = soup.find('table', id="data-table-default")
print(table)

headers = table.find_all("th")
print(headers)

titles = []

for i in headers:
  title = i.text
  titles.append(title)

print(titles)

df = pd.DataFrame(columns = titles)
for j in table.find_all("tr")[1:]:
 row_data = j.find_all("td")
 row = [i.text for i in row_data]
 length = len(df)
 row = df.loc[length]
 print(row)
 rows = table.find_all("tr")

 for i in rows[1:]:
     data = i.find_all("td")
     print(data)
     row = [tr.text for tr in data]
     print(row)
     l = len(df)
     df.loc[l] = row

 df.to_csv("test.csv")