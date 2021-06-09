import requests
from bs4 import BeautifulSoup
products_to_track = [
{
  "prod_url":"https://www.amazon.in/Samsung-Galaxy-M12-Storage-Processor/dp/B08XGDN3TZ/ref=sxin_2_hcs-la-in-1?cv_ct_cx=samsung&dchild=1&keywords=samsung&pd_rd_i=B08XGDN3TZ&pd_rd_r=c900ad71-0c85-42b4-ac6a-f160ba04cd17&pd_rd_w=xibBi&pd_rd_wg=tH9so&pf_rd_p=b6d118af-97d2-4a68-bf40-4cd2a7c6b3cd&pf_rd_r=YPXSPHC5F3NZQRRG0DJS&qid=1623138297&sr=1-1-99b054f1-0e42-4e3b-b375-028105b26bc6",
  "name":"Samsung Galaxy M12 Blue,4GB RAM, 64GB",
  "target_price":11000
 },
{
 "prod_url":"https://www.amazon.in/Samsung-Galaxy-Storage-Triple-Camera/dp/B08RSY2653/ref=sxin_2_hcs-la-in-1?cv_ct_cx=samsung&dchild=1&keywords=samsung&pd_rd_i=B08RSY2653&pd_rd_r=c900ad71-0c85-42b4-ac6a-f160ba04cd17&pd_rd_w=xibBi&pd_rd_wg=tH9so&pf_rd_p=b6d118af-97d2-4a68-bf40-4cd2a7c6b3cd&pf_rd_r=YPXSPHC5F3NZQRRG0DJS&qid=1623138297&sr=1-4-99b054f1-0e42-4e3b-b375-028105b26bc6",
 "name":"Samsung Galaxy M02s Blue,4GB RAM, 64GB",
"target_price":9000
},
{
 "prod_url":"https://www.amazon.in/Samsung-Galaxy-M12-Storage-Processor/dp/B08XJG8MQM/ref=sr_1_6?dchild=1&keywords=samsung&qid=1623138297&sr=8-6",
 "name":"Samsung Galaxy M12 Blue,6GB RAM, 128GB",
"target_price":13000
},
{
 "prod_url":"https://www.amazon.in/Samsung-Galaxy-Storage-Additional-Exchange/dp/B086KCC68B/ref=sr_1_7?dchild=1&keywords=samsung&qid=1623138297&sr=8-7",
 "name":"Samsung Galaxy M11 Violet, 4GB RAM, 64GB Storage",
"target_price":9500
}

]


def give_prod_price(URL):
     headers = {
                 "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.77 Safari/537.36"
              }
     page = requests.get(URL, headers=headers)

     soup = BeautifulSoup(page.content, 'html.parser')
     prod_price = soup.find(id="priceblock_dealprice")
     if (prod_price == None):
       prod_price = soup.find(id="priceblock_ourprice")
     return prod_price.getText()

result_file= open('result_file.txt','w')
for every_prod in products_to_track:
    prod_price_returned = give_prod_price(every_prod.get("prod_url"))
    print(prod_price_returned+'-'+every_prod.get("name"))
    my_prod_price= prod_price_returned[2:]
    my_prod_price= my_prod_price.replace(',','')
    my_prod_price=int(float(my_prod_price))
    print(my_prod_price)
    if my_prod_price<every_prod.get("target_price"):
      print("available at your required price")
      result_file.write(every_prod.get("name")+'-\t'+"available at target price,"+"current price "+str(my_prod_price)+'\n')
    else:
      print("Still not at your required price")
