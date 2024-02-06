from playwright.sync_api import Page

class ProductPage:
    
    def __init__(self,page:Page):
        self.page=page
        self.product_page_label = page.inner_text(".product_label")
        
    def verify_product_page(self):
        self.product_page_label == "Products"