import requests
import json
from bs4 import BeautifulSoup

# 목표는, 멤버들 블로그 전체 게시글 가져오기
# 아이디를 넣으면, 그 아이디의 블로그 전체 게시글 제목들을 가져오는 함수 구현

def get_blog_posts(id):
    print(id + " 이놈아 뜯어보겄소")
    url = data['tistory-left'] + id + data['tistory-right']
    req = requests.get(url)
    
    soup = BeautifulSoup(req.content, 'html.parser')
    
    res = soup.select('#mArticle > div > a.link_post > strong')

    if len(res) == 0:
        print("아무도 없구려")
    else:
        for i in res:
            print("-", i.contents[0])
    
    print("")
  
      
def blogpost_crawler(data):
    for i in data['member']:
        get_blog_posts(i)

        
if __name__ == "__main__":
    
    with open('./data.json', 'r', encoding='utf-8') as f:
        data = json.load(f)
    blogpost_crawler(data)