# Old Tweet Scraper

## Details
Old Tweet Scraper adalah program yang digunakan untuk mendapatkan data tweet lama tanpa autentikasi Twitter API.
Telah kita ketahui Twitter API standar memiliki keterbatasan dalam mendapatakan data tweet lama, tweet dengan jangka lebih dari satu minggu tidak bisa didapatkan menggunakan Twitter API. Old Tweet Scraper mampu mendapatkan data tweet lama, bahkan untuk tweet beberapa tahun silam. Keuntungan lain dari Old Tweet Scraper adalah kita tidak perlu menggunakan autentikasi dari Twitter API dan tidak perlu login dengan akun twitter.

## Cara menggunakan
Untuk daat menggunakan program ini, kita bisa melakukan Git clone atau mendownloadnya sebagai ZIP.
Buka terminal atau command prompt dan arahkan direktori ke direktoi yang telah didownload.

### Contoh:
* Mendapatkan tweet dengan kata kunci tertentu dan menyimpannya ke dalaam folder yang kita buat
```bash
TweetScraper.py --querysearch "Politics" --foldername "politics"
```
* Mendapatkan tweet dengan lebih dari satu kata kunci dan menyimpannya ke dalaam folder yang kita buat
```bash
TweetScraper.py --querysearch "(\\"Donald Trump\\" OR \\"Joe Biden\\") lang:id since:2020-12-30" --foldername "politics"
```
* Mendapatkan tweet dengan jumlah yang dibatasi (100 tweets)
```bash
TweetScraper.py --querysearch "Politics" --foldername "politics" --limited
```
* Mendapatkan tweet dengan jumlah yang dibatasi sesuai jumlah yang kita inginkan
```bash
TweetScraper.py --querysearch "Politics" --foldername "politics" --limited --maxtweets 200
```

Masing-masing tweet akan tersimpan di dalam folder data atau data/foldername jika kita memberikan nama folder yang kita inginkan. File yang tersimpan memiliki format JSON yang berisi:

* 'date'
* 'username'
* 'fullname'
* 'verified'
* 'followers'
* 'id'
* 'replies'
* 'retweets'
* 'favorites'
* 'tweet'
* 'mentions'
* 'hashtags'
* 'permalink'
* 'replyTo'
* 'quoteUrl'
* 'quoteFrom'
* 'photos'
* 'lang'
* 'source'
* 'place'
