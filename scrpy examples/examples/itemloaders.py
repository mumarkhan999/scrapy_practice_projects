from scrapy.loader import ItemLoader
from scrapy.loader.processors import TakeFirst, MapCompose, Join
from items import Quote


class QuoteLoader(ItemLoader):

    default_output_processor = TakeFirst()
    default_item_class = Quote
    # for o/p processor
    # tag_out
    tags_in = MapCompose()