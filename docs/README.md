# 台股資料爬蟲 (python2.7)

## 實作規格

### 股票代碼

POST

http://mops.twse.com.tw/mops/web/ajax_t51sb01

```json
payload = {
  'encodeURIComponent': 1,
  'step': 1,
  'firstin': 1,
  'TYPEK': 'otc', # sii/otc
  'code': '',
}
```
POST

http://mops.twse.com.tw/server-java/t105sb02

```json
payload = {
  'firstin', # hidden inputs from previous html
  'step', # hidden inputs from previous html
  'filename', # hidden inputs from previous html
}
```
### 集保戶股權分散表(股狗)

GET

https://www.stockdog.com.tw/stockdog/index.php

``` json
params = {
    'sid', # 股票代碼
    'p': 7,
    'm': 1,
}
```

GET

https://www.stockdog.com.tw/stockdog/ajax.php

``` json
params = {
  'Atype', # Atype in function ajax_table from previous html
  'type': 0, # 1/2/3
  'sid', # 股票代碼
}
```

- 用 Chrome 的 headers
- Cookie
  - G\_AUTHUSER\_H=0
  - G\_ENABLED\_IDPS=google
  - SDSSESSID

