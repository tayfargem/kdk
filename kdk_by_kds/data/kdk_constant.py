url = "https://kararlar.ombudsman.gov.tr/Arama/IndexPaging"

headers = {
    "Accept": "application/json, text/javascript, */*; q=0.01",
    "Accept-Encoding": "gzip,deflate,br",
    "Accept-Language": "tr-TR,tr;q=0.8,en-US;q=0.5,en;q=0.3",
    "Connection": "keep-alive",
    "Content-Length": "1556",
    "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
    "DNT": "1",
    "Host": "kararlar.ombudsman.gov.tr",
    "Origin": "https://kararlar.ombudsman.gov.tr/",
    "Referer": "https://kararlar.ombudsman.gov.tr/Arama/Index",
    "Sec-Fetch-Dest": "empty",
    "Sec-Fetch-Mode": "cors",
    "Sec-Fetch-Site": "same-origin",
    "User-Agent": "Mozilla/5.0 (X11; Linux x86_64; rv:109.0) Gecko/20100101 Firefox/118.0",
    "X-Requested-With": "XMLHttpRequest",
}

data_def = {"draw": "1",
            "columns[0][data]": "sikayeT_NO",
            "columns[0][name]": "",
            "columns[0][searchable]": "true",
            "columns[0][orderable]": "true",
            "columns[0][search][value]": "",
            "columns[0][search][regex]": "false",
            "columns[1][data]": "karaR_TARIH",
            "columns[1][name]": "",
            "columns[1][searchable]": "true",
            "columns[1][orderable]": "true",
            "columns[1][search][value]": "",
            "columns[1][search][regex]": "false",
            "columns[2][data]": "karaR_TURU",
            "columns[2][name]": "",
            "columns[2][searchable]": "true",
            "columns[2][orderable]": "true",
            "columns[2][search][value]": "",
            "columns[2][search][regex]": "false",
            "columns[3][data]": "evraK_KONU",
            "columns[3][name]": "",
            "columns[3][searchable]": "true",
            "columns[3][orderable]": "true",
            "columns[3][search][value]": "",
            "columns[3][search][regex]": "false",
            "columns[4][data]": "sikayeT_EDILEN_KURUM",
            "columns[4][name]": "",
            "columns[4][searchable]": "true",
            "columns[4][orderable]": "true",
            "columns[4][search][value]": "",
            "columns[4][search][regex]": "false",
            "columns[5][data]": "evraK_ID",
            "columns[5][name]": "",
            "columns[5][searchable]": "true",
            "columns[5][orderable]": "true",
            "columns[5][search][value]": "",
            "columns[5][search][regex]": "false",
            "order[0][column]": "0",
            "order[0][dir]": "desc",
            "start": "0",
            "length": "10",
            "search[value]": "",
            "search[regex]": "false",
            "basbas": "",
            "basbit": "",
            "basnoyil": "",
            "basnosayi": "",
            "sikayetkonu": "",
            "konuidarekelimeleri": "",
            "karbas": "",
            "karbit": "",
            "kararTuru": "",
            "evrakkonu": "",
            "ortakalankelimeleri": ""
            }
