# Youget-Biibii-OldBoy
我是透過B站入門Python的，  
一方面怕B站下架此系列影片，另一方面其實自己學習狀況較不佳  
想藉由快速撥放的方式複習，因此藉由Youget模塊將系列影片爬取製本地撥放複習。  
[soimort/you-get](https://github.com/soimort/you-get)  


## 不足之處
這次爬取時遇到如下圖所示，影片選集列表由JS生成，因此使用bs4中的lxml爬取到網址，
比較好的作法應使用Scrapy爬蟲框架爬取，  

![](https://i.imgur.com/jpFaozW.png)