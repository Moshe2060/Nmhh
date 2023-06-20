import requests

import webbrowser

from bs4 import BeautifulSoup

import xml.etree.ElementTree as ET

url = "https://seret.fun/main/watch/movie/20443/%D7%94%D7%90%D7%97%D7%99%D7%9D_%D7%A1%D7%95%D7%A4%D7%A8_%D7%9E%D7%A8%D7%99%D7%95%3A_%D7%94%D7%A1%D7%A8%D7%98"

response = requests.get(url)

html_content = response.text

# ×¤×™×¨×•×§ ×“×£ ×”×œ×•×— ×©×™×“×•×¨×™×

ht = BeautifulSoup(html_content, "html.parser")

set1 = ""

noPremium = ht.select('video')

if "series" in url:

    set1 = noPremium[1]

else:

    set1 = noPremium[0]

set2 = set1.get("src")

split1 = set2.split(".")

replace1 = split1[2].replace(split1[2], split1[2] + "_premium")

utlP = f'\n{split1[0] + "." + split1[1] + "." + replace1 + "." + split1[3]}'

webbrowser.open(utlP)

# print(f'\n{split1[0]+"."+split1[1]+"."+replace1+"."+split1[3]}')
