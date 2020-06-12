import requests
import bs4
import lxml 

response = requests.get("https://www.snapdeal.com/search?keyword=jeans&santizedKeyword=&catId=&categoryId=0&suggested=false&vertical=&noOfResults=20&searchState=&clickSrc=go_header&lastKeyword=&prodCatId=&changeBackToAll=false&foundInAll=false&categoryIdSearched=&cityPageUrl=&categoryUrl=&url=&utmContent=&dealDetail=&sort=rlvncy&q=Size_s%3A28%7CFit_s%3ASlim%7C")
response = response.text
data = bs4.BeautifulSoup(response,'lxml')

read = data.select(".picture-elem ")
# print(len(read))
# print(read[0])
for i in read :
    product_name = i.select(".product-image")
    print("product_name :",product_name  )

    

















# import requests
# import bs4
# import lxml 

# response = requests.get("https://www.snapdeal.com/search?keyword=jeans&santizedKeyword=&catId=&categoryId=0&suggested=false&vertical=&noOfResults=20&searchState=&clickSrc=go_header&lastKeyword=&prodCatId=&changeBackToAll=false&foundInAll=false&categoryIdSearched=&cityPageUrl=&categoryUrl=&url=&utmContent=&dealDetail=&sort=rlvncy&q=Size_s%3A28%7CFit_s%3ASlim%7C")
# response = response.text
# data = bs4.BeautifulSoup(response,'lxml')

# read = data.select(".product-tuple-image ")

# z = []
# for i in read:
#     x = list(i)
#     z.append(x)
# print(z)
