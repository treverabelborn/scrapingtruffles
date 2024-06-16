from itemadapter import ItemAdapter


class TruffleProductPipeline:
    def open_spider(self, spider):
        self.file = open("sabatino_products.csv", "w")
        self.file.write("description,price\n")

    def close_spider(self, spider):
        self.file.close()

    def process_item(self, item, spider):
        adapter = ItemAdapter(item)
        self.file.write("{},{}\n".format(adapter.get("description"), adapter.get("price")))
        return item
