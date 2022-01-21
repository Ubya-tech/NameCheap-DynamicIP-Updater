# NameCheap-DynamicIP-Updater
  [![HitCount](http://hits.dwyl.com/Ubya-tech/NameCheap-DynamicIP-Updater.svg?style=flat-square)](http://hits.dwyl.com/Ubya-tech/NameCheap-DynamicIP-Updater)[![HitCount](http://hits.dwyl.com/Ubya-tech/NameCheap-DynamicIP-Updater.svg?style=flat-square&show=unique)](http://hits.dwyl.com/Ubya-tech/NameCheap-DynamicIP-Updater)
## What's the point of this script?
NameCheap already offers a client you can [download](https://namecheap.simplekb.com/SiteContents/2-7C22D5236A4543EB827F3BD8936E153E/media/Dynamic%20DNS%20Client%20%202.0.0.7%20Beta.zip), but i didn't want to have my computer running 24/7 just for it.

I have a Raspberry PI Zero W i use for general automation, so i made this little script to be run there.
I didn't include a timer inside the script itself, since i'm using *Cron* to run the script every minute.
