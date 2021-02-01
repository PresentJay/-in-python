import requests
import json
from bs4 import BeautifulSoup

# 목표는, 멤버들 블로그 전체 게시글 가져오기
# 아이디를 넣으면, 그 아이디의 블로그 전체 게시글 제목들을 가져오는 함수 구현

def get_blog_posts(data, id):
    print(id + " 이놈아 뜯어보겄소")
    
    url = data['tistory-left'] + id + data['tistory-right'] 
    req = requests.get(url + data['whole-board'])
    counter = 1
    while True:
        soup = BeautifulSoup(req.content, 'html.parser')
        for parser in data['post-std']:
            res = soup.select('.' + parser)
            if len(res) > 0:
                for i in res:
                    print("-", i)
        
        if len(soup.select('.no-more-next')) > 0 or len(soup.select('area-paging-more-end')) > 0:
            break
        else:
            counter += 1
            req = requests.get(url + data['page-std'] + str(counter))
    
      
def blogpost_crawler(data):
    for i in data['member']:
        get_blog_posts(data, i)

        
if __name__ == "__main__":
    
    with open('./data.json', 'r', encoding='utf-8') as f:
        data = json.load(f)
    blogpost_crawler(data)