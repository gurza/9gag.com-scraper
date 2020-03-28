9gag.com scraper
================

Client tool to scrape media posts from [9gag.com](https://9gag.com).  
Infinite scrolling is supported.


## Usage
Let's scrape posts from [https://9gag.com/search?query=coronavirus](https://9gag.com/search?query=coronavirus).


```console
$ pip install -r requirements.txt
$ scrapy runspider ninegag_spider.py -a query=coronavirus -o out/coronavirus.json
```

Output
```console
$ head ./out/coronavirus.json 
[
{"id": "aY701r0", "title": "Coronavirus", "url": "https://img-9gag-fun.9cache.com/photo/aY701r0_700b.jpg"},
{"id": "a3ROMWQ", "title": "Coronavirus", "url": "https://img-9gag-fun.9cache.com/photo/a3ROMWQ_700b.jpg"},
{"id": "a5R0QGO", "title": "Coronavirus", "url": "https://img-9gag-fun.9cache.com/photo/a5R0QGO_700b.jpg"},
{"id": "a85xLoQ", "title": "Coronavirus Combo Holiday", "url": "https://img-9gag-fun.9cache.com/photo/a85xLoQ_700b.jpg"},
{"id": "an5oEG5", "title": "Coronavirus everywhere.", "url": "https://img-9gag-fun.9cache.com/photo/an5oEG5_460sv.mp4"},
{"id": "ap5MvxW", "title": "Dr. Fauci Dies Inside - White House Press Conference 3/20/2020", "url": "https://img-9gag-fun.9cache.com/photo/ap5MvxW_460sv.mp4"},
{"id": "aZ7YKAV", "title": "Uk vs coronavirus", "url": "https://img-9gag-fun.9cache.com/photo/aZ7YKAV_460sv.mp4"},
{"id": "aj5eB9p", "title": "Asia VS Coronavirus", "url": "https://img-9gag-fun.9cache.com/photo/aj5eB9p_460sv.mp4"},
{"id": "aV06DnM", "title": "Not a coronavirus post", "url": "https://img-9gag-fun.9cache.com/photo/aV06DnM_700b.jpg"},
```
