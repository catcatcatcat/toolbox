# 貓貓工具箱 toolbox

一堆單頁小工具。每個都是一個 HTML 檔、零依賴、離線可用，資料全部留在瀏覽器裡。

線上版：<https://toolbox.catcatcatcat.cc>

## 工具

| 路徑 | 說明 |
|---|---|
| [`zine-fold/`](zine-fold/) | 八折小誌拼版器——把 8 張頁面圖排進一張 A4 橫向紙，列印後折三次、剪一刀就是一本 8 頁小誌 |

## 做法

沒有框架、沒有 build step、沒有後端。每個工具就是一份 HTML，用瀏覽器直接打開即可，
也可以存成檔案帶著走。想在本機預覽整站：

```
python3 -m http.server 4180
```

然後開 <http://localhost:4180>。

## 隱私

工具不會把你的檔案送到任何地方。程式碼裡沒有 `fetch`、沒有 `XMLHttpRequest`、沒有後端，
設定留在 `localStorage`、圖片留在 `IndexedDB`，兩者都在你自己的瀏覽器裡。

**零第三方請求**：字型直接內嵌在 HTML 裡，不走 Google Fonts CDN，所以沒有任何一個
外部網域會看到訪客 IP。頁面存成本機檔案後離線打開，外觀與功能完全一樣。

自己驗證：開發者工具 Network 分頁重新整理頁面，除了頁面本身不該出現任何請求；
或在 Console 執行 `performance.getEntriesByType('resource')`，應該回傳空陣列。

## 授權

程式碼以 [MIT License](LICENSE) 釋出。

字型內嵌在頁面裡，等同隨本專案散布，因此附上授權全文與版權宣告。兩者皆採
[SIL Open Font License 1.1](https://openfontlicense.org/)：

| 字型 | 版權 | 授權全文 |
|---|---|---|
| Archivo | Copyright 2020 The Archivo Project Authors ([Omnibus-Type/Archivo](https://github.com/Omnibus-Type/Archivo)) | [`fonts/OFL-Archivo.txt`](fonts/OFL-Archivo.txt) |
| IBM Plex Sans／Mono | Copyright © 2017 IBM Corp. with Reserved Font Name "Plex" | [`fonts/OFL-IBM-Plex.txt`](fonts/OFL-IBM-Plex.txt) |

OFL 允許內嵌與再散布，但要求保留版權宣告與授權全文，**請勿刪除 `fonts/OFL-*.txt`**。

字型來源檔與內嵌腳本住在 [`fonts/`](fonts/)。改動字型設定後重新產生內嵌區塊：

```
python3 fonts/build-fonts.py           # 用本機 .woff2 重建頁面
python3 fonts/build-fonts.py --fetch   # 先重新下載字型再重建
```

腳本只會覆寫每個頁面裡 `<!-- fonts:begin -->` 到 `<!-- fonts:end -->` 之間的內容。
