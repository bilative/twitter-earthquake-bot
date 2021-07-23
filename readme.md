## Hi
I wanna make a twitter bot. This bot gonna tweet if there is a earthquake in last 1 min.

I wanted to do this bc you know, when we feel smth like shaking, we are checking 'website of Kandilli Rasathanesi' (this is one of the main reporter of earthquake in Turkey).
This application will check website of [BOĞAZİÇİ ÜNİVERSİTESİ KANDİLLİ RASATHANESİ VE DEPREM ARAŞTIRMA ENSTİTÜSÜ (KRDAE)](http://www.koeri.boun.edu.tr/scripts/lst9.asp) and if there is a new earthquake it'll tweet it with details.

We can filter the tweets by some specific regions (like EGE), and we can send messages maybe.

----

I used some web scrabing methods for this. And I took twitter developer account to use API. And I have a project app named _**bilative**_.

You can find some tweets from the app. My twitter API name is bilative. You can see name of the app on informations of tweet.
* [02:39:41](https://twitter.com/bilallozdemir/status/1418358508135796743)
* [03:02:46](https://twitter.com/bilallozdemir/status/1418363074785026053)
![rt](https://user-images.githubusercontent.com/70684994/126724391-1aefdb2e-3658-41f5-9eaf-85014d15d1de.png)
----
There is some details about bot.
* Informations about earthquakes comes to website of Kandilli little late. So if eartquake occured at 03:02, website of Kandilli report it at 03:11.
* Because of this latency our tweet system is also tweet late.
* Our system is as fast as Kandilli Rasathanesi.

Some screenshoots from app and website of [Kandilli Rasathanesi](http://www.koeri.boun.edu.tr/scripts/lst9.asp):

![apppppppppp](https://user-images.githubusercontent.com/70684994/126724428-f51874fd-6cef-4e14-8edc-477258679cab.png)
![02_53later](https://user-images.githubusercontent.com/70684994/126724449-42704b07-ddc9-41fb-813a-1d7c1e8d74ff.png)

## This was only a test app for me. This app could run on server 24/7 and twitter bot account could collect some followers on twitter. Why not??
