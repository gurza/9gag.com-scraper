# -*- coding: utf-8 -*-
import json

import scrapy


class NinegagSpider(scrapy.Spider):
    name = 'ninegag'
    posts_base_url = 'https://9gag.com/v1/search-posts?query=%s&c=%s'

    def __init__(self, query='', **kwargs):
        self.count = 0
        self.query = query
        self.start_urls = [self.posts_base_url % (self.query, self.count)]
        super().__init__(**kwargs)

    def parse(self, response):
        data = json.loads(response.body)

        cnt = 0
        for post in data.get('data', {}).get('posts', []):
            cnt += 1

            url = None
            post_type = post.get('type')
            if post_type == 'Photo':
                url = post.get('images', {}).get('image700', {}).get('url')
            elif post_type == 'Animated':
                url = post.get('images', {}).get('image460sv', {}).get('url')

            yield {
                'id': post.get('id'),
                'title': post.get('title'),
                'url': url,
            }

        if cnt > 0:
            self.count += cnt
            yield scrapy.Request(self.posts_base_url % (self.query, self.count))
