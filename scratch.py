import requests
from bs4 import BeautifulSoup
Youtube_trending='https://www.youtube.com/feed/trending'

response=requests.get(Youtube_trending)
print('Status Code',response.status_code)

doc = BeautifulSoup(response.text,'html.parser')
print('Page title:',doc.title.text)

video_divs=doc.find_all('div',class_='ytd-video-renderer')
print(f'Found{len(video_divs)}videos')