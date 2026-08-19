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
圖片與設定全程留在你自己的瀏覽器（`localStorage`）。

唯一的外部請求是 Google Fonts CDN 載入字型，這會讓 Google 看到訪客 IP。
不想要的話，把頁面存成本機檔案離線開啟即可（字型會退回系統預設字體，功能不受影響）。

## 授權

程式碼以 [MIT License](LICENSE) 釋出。

字型 Archivo 與 IBM Plex 由 Google Fonts CDN 載入，非本專案散布，兩者皆採
SIL Open Font License 1.1。
