## TFMediumBlogCrawling
### 1.浏览网页，分析网页结构
> 网页地址：https://medium.com/tag/software-engineering/archive  
> 利用google开发者工具copy相应内容标签的selector或者xpath  
> 比如，文章标题的element xpath：**//*[@id="root"]/div/div[3]/div[2]/div/div[4]/div/div[3]/div[1]/div/article/div/div/div/div/div[2]**  
> 点赞数对应的element xpath： **//*[@id="root"]/div/div[3]/div[2]/div/div[4]/div/div[3]/div[1]/div/article/div/div/div/div/div[3]/div/div[1]**  
>  
> **Tips:** 网页结构可能随时发生变化，导致抓取的代码无法正常运行。所以需要定期检查网页结构，并更新抓取代码。  
> 
### 2.抓取网页数据
> 使用python selenium模拟人工访问网页（规避网站的反爬虫机制），选择<10 most read>，拉取这10篇文章的url  
> 比如第一篇文章链接的element xpath: //*[@id="root"]/div/div[3]/div[2]/div/div[4]/div/div[3]/div[1]/div/article/div/div/div/div/div[2]/div[1]/a[@href]  
> 
> 根据url访问正文，获取文章内容  
> 正文的element xpath:  //*[@id="root"]/div/div[3]/div[2]/div[2]/article/div/div/section/div/div[3]/div/div  
> 
>  **Tips:** 合理设置抓取程序的访问频率、超时时间  
>  
### 3.调用三方API进行翻译
> pip install googletrans==4.0.0rc1  
> 使用google\百度 API翻译，需要注册API key  

### 其他工具
+  本地谷歌浏览器安装目录：C:\Program Files\Google\Chrome\Application
+  取到目录 "119.0.6045.160" 就是你现在本地谷歌浏览器的版本
+  只取版本最前面的 "119", 跳转到链接 "https://googlechromelabs.github.io/chrome-for-testing/LATEST_RELEASE_119", 返回的文本内容 "119.0.6045.105" 就是 `driver 版本`。
+ （4）下载Chromedriver.exe链接："https://edgedl.me.gvt1.com/edgedl/chrome/chrome-for-testing/119.0.6045.105/win64/chromedriver-win64.zip"。
