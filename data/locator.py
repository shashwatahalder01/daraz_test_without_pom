from selenium import webdriver
from selenium.webdriver.common.keys import Keys


loginlink='//*[@id="anonLogin"]/a'
usernameinput = '//*[@id="container"]/div/div[2]/form/div/div[1]/div[1]/input'
userpasswordinput = '//*[@id="container"]/div/div[2]/form/div/div[1]/div[2]/input'
loginbtn = '//*[@id="container"]/div/div[2]/form/div/div[2]/div[1]/button'

searchproduct = "q"

brandcheckbox = '//*[@id="root"]/div/div[2]/div[1]/div/div[2]/div/div[2]/div[2]/div/div[1]/label[4]/span[1]/input'
servicechebox = '//*[@id="root"]/div/div[2]/div[1]/div/div[2]/div/div[3]/div[2]/div/div/label[2]/span[1]/input'

productlist = 'c16H9d'


productlink = '//*[@id="root"]/div/div[2]/div[1]/div/div[1]/div[2]/div[1]/div/div/div[1]/div/a'

productname = '//*[@id="module_product_title_1"]/div/div/span'
productbrand = '//*[@id="module_product_brand_1"]/div/a[1]'

addtocartbtn = '//*[@id="module_add_to_cart"]/div/button[2]'
gotocartbtn = '//*[@id="dialog-body-1"]/div/div[1]/div/div[2]/div/div[2]/div/div[2]/button[2]'

# cartproductname ='automation-link-from-title-to-prod title'
# cartproductbrand = 'automation-link-from-sub-title-to-prod sku'
cartproductname = '//div//div//div//div//div//div//div//div//div//div//div[2]//a[1]'
cartproductbrand= '//body/div/div/div/div/div/div/div/div/div/div/div/div/div/a[2]'

affilitatelink = '//*[@id="anonSignup"]/a'

affiliatepageurl = '//*[@id="J_6558113530"]/div/div/p[5]/a[1]'

helpcenterlink = '//*[@id="J_1362278930"]/section/div[1]/div/div[1]/ul[1]/li[1]/a'
howtobuylink = '//*[@id="J_1362278930"]/section/div[1]/div/div[1]/ul[1]/li[2]/a'
returnndgoodslink = '//*[@id="J_1362278930"]/section/div[1]/div/div[1]/ul[1]/li[4]/a'
contactuslink = '//*[@id="J_1362278930"]/section/div[1]/div/div[1]/ul[1]/li[5]/a'








