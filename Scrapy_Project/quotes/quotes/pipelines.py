# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface

class QuotesPipeline:

    def process_item(self, item, spider):
        with open("quote.xlsx", "a", encoding="utf-8") as excel_file:
            if excel_file.tell() == 0:
                header = "quote\tbirthdate\ttags\tlocation\tdescription\tname\n"
                excel_file.write(header)

            row = "\t".join([item['quote'], item['birthdate'], item['tags'], item['location'], item['description'], item['name']])
            excel_file.write(f"{row}\n")
