# Catcat Toolbox / 貓貓工具箱

[English](#english) · [繁體中文](#繁體中文)

## English

A collection of small, single-page tools. Each tool is one HTML file with no dependencies, works offline, and keeps your data in your browser.

Try it online: <https://toolbox.catcatcatcat.cc>

### Maintenance status

🟢 **Actively maintained.** New single-page tools and fixes are added over time.

### Tools

| Path | Description |
|---|---|
| `zine-fold/` | **Eight-page zine imposition tool** — Arrange eight page images on one landscape A4 sheet. Fold it three times and make one cut to create an eight-page zine. |
| `id-photo-sheet/` | **Photo booth-style ID sheet generator** — Turn one photo into a 2×4 sheet of eight portraits, with customizable name, date, purpose, and serial number. |
| `budget-quest/` | **Moonlight Cat: Budget Survival** — Treat 1–10 budget pools as health bars, record spending and savings, and export a local backup. |
| `receipt-maker/` | **Receipt generator** — Enter the recipient, purpose, and amount to create an A4 receipt. Supports cash or bank transfer, optional tax withholding, printing, and PDF export. |
| `speaker-timer/` | **Speaker timer** — A large countdown display for event speakers. It plays one alert at a chosen remaining time and another at zero, then switches to a red overtime counter. Full-screen mode is included. |

### How it works

There is no framework, build step, or backend. Each tool is a standalone HTML file that you can open directly in a browser or save locally for later use.

To preview the whole site locally:

```sh
python3 -m http.server 4180
```

Then open <http://localhost:4180>.

### Privacy

The tools do not send your files or form contents anywhere. There is no `fetch`, `XMLHttpRequest`, or backend in the code.

- `zine-fold` stores settings in `localStorage` and page images in `IndexedDB`.
- `id-photo-sheet` does not save your photo; it is cleared when you close the tab.
- `budget-quest` stores your budget data in `localStorage`; backups are exported only when you choose to download them.
- `receipt-maker` stores reusable document fields such as the title, payer, purpose, tax settings, payment method, and note in `localStorage`. Names, national ID numbers, addresses, and bank account numbers are not retained.
- `speaker-timer` stores only the talk duration and alert-sound preferences. Its sounds are synthesized by the browser, so no audio files are loaded.

All of this data stays in your own browser.

The **Copy return link** feature in `receipt-maker` encodes the completed form in the URL fragment after `#`. URL fragments are not sent to the server as part of an HTTP request, so the encoded content passes only through the channel you use to share the link. The link may still remain in chat or email history, so share it only with trusted recipients when it contains sensitive personal information.

**Tool data stays in the browser:** fonts are embedded directly in the HTML instead of being loaded from Google Fonts. The current tool pages make no third-party resource requests. Even if ads are added in the future, the images, text, and files you provide to a tool will not be shared with an advertising service. If you save a page as a local HTML file, its core features and appearance will continue to work offline.

To verify this yourself, reload a tool with the Network panel in your browser's developer tools open. You should see no requests other than the page itself. You can also run the following in the Console; it should return an empty array:

```js
performance.getEntriesByType('resource')
```

### License

The code is released under the [MIT License](LICENSE).

The fonts are embedded in the pages and distributed with this repository, so their full license texts and copyright notices are included. Both use the [SIL Open Font License 1.1](https://openfontlicense.org/):

| Font | Copyright | License text |
|---|---|---|
| Archivo | Copyright 2020 The Archivo Project Authors ([Omnibus-Type/Archivo](https://github.com/Omnibus-Type/Archivo)) | [fonts/OFL-Archivo.txt](fonts/OFL-Archivo.txt) |
| IBM Plex Sans / Mono | Copyright © 2017 IBM Corp. with Reserved Font Name "Plex" | [fonts/OFL-IBM-Plex.txt](fonts/OFL-IBM-Plex.txt) |

The OFL permits embedding and redistribution, but requires the copyright notices and full license texts to remain available. **Do not remove `fonts/OFL-*.txt`.**

Font source files and the embedding script live in `fonts/`. After changing the font configuration, regenerate the embedded font blocks with:

```sh
python3 fonts/build-fonts.py          # Rebuild pages from local .woff2 files
python3 fonts/build-fonts.py --fetch  # Download the fonts again, then rebuild
```

The script only replaces content between `<!-- fonts:begin -->` and `<!-- fonts:end -->` in each page.

---

## 繁體中文

一堆單頁小工具。每個都是一個 HTML 檔、零依賴、離線可用，資料全部留在瀏覽器裡。

線上版：<https://toolbox.catcatcatcat.cc>

### 維護狀態

🟢 **目前維護中。** 持續新增與修正單頁小工具。

### 工具

| 路徑 | 說明 |
|---|---|
| `zine-fold/` | 八折小誌拼版器——把 8 張頁面圖排進一張 A4 橫向紙，列印後折三次、剪一刀就是一本 8 頁小誌 |
| `id-photo-sheet/` | 證明寫真風圖片產生器——一張照片排成 2×4 八格相片，可調姓名、日期、用途與流水號 |
| `budget-quest/` | 月光貓貓：預算生存記帳——把 1–10 個預算池當成生命條，記帳、節約、匯出本機備份 |
| `receipt-maker/` | 領據產生器——填好抬頭、事由與金額排成一張 A4 領據，付款方式可選現金或匯款，可選代扣稅額，戶籍地址會提示要寫到鄰里，直接列印或存成 PDF |
| `speaker-timer/` | 講者計時器——給活動講者看的超大倒數，剩下設定的時間時響一次提醒音，時間到再響一次，超時改成紅色往上加，可鋪滿整個螢幕 |

### 做法

沒有框架、沒有 build step、沒有後端。每個工具就是一份 HTML，用瀏覽器直接打開即可，也可以存成檔案帶著走。想在本機預覽整站：

```sh
python3 -m http.server 4180
```

然後開啟 <http://localhost:4180>。

### 隱私

工具不會把你的檔案或表單內容送到任何地方。程式碼裡沒有 `fetch`、沒有 `XMLHttpRequest`、沒有後端。

- `zine-fold` 的設定留在 `localStorage`，頁面圖片留在 `IndexedDB`。
- `id-photo-sheet` 連照片都不保存，關閉分頁即清除。
- `budget-quest` 將預算資料留在 `localStorage`；只有你主動下載時才會匯出備份。
- `receipt-maker` 會把文件標題、抬頭、事由、稅額設定、付款方式與備註等可重複使用的欄位寫進 `localStorage`，姓名、身分證字號、地址與帳號不留存。
- `speaker-timer` 只記演講長度與提醒音偏好，提醒音是瀏覽器即時合成的，沒有音檔。

這些資料都只存在使用者自己的瀏覽器裡。

`receipt-maker` 的「複製回傳連結」把填好的內容編碼在網址的 `#` 片段裡。依 HTTP 規格，`#` 之後的內容不會送給伺服器，所以連結只在你和收件者之間傳遞；但它畢竟是一段網址，會留在你貼上的聊天室或信件裡，個資敏感時請只傳給信任的對象。

**工具資料留在瀏覽器裡**：字型直接內嵌在 HTML 裡，不走 Google Fonts CDN；目前工具頁沒有第三方請求。即使未來加入廣告，使用者放進工具的圖片、文字與檔案也不會交給廣告服務。頁面存成本機檔案後離線打開，核心功能與外觀仍可使用。

自己驗證：開發者工具 Network 分頁重新整理頁面，除了頁面本身不該出現任何請求；或在 Console 執行下列程式，應該回傳空陣列：

```js
performance.getEntriesByType('resource')
```

### 授權

程式碼以 [MIT License](LICENSE) 釋出。

字型內嵌在頁面裡，等同隨本專案散布，因此附上授權全文與版權宣告。兩者皆採 [SIL Open Font License 1.1](https://openfontlicense.org/)：

| 字型 | 版權 | 授權全文 |
|---|---|---|
| Archivo | Copyright 2020 The Archivo Project Authors ([Omnibus-Type/Archivo](https://github.com/Omnibus-Type/Archivo)) | [fonts/OFL-Archivo.txt](fonts/OFL-Archivo.txt) |
| IBM Plex Sans／Mono | Copyright © 2017 IBM Corp. with Reserved Font Name "Plex" | [fonts/OFL-IBM-Plex.txt](fonts/OFL-IBM-Plex.txt) |

OFL 允許內嵌與再散布，但要求保留版權宣告與授權全文，**請勿刪除 `fonts/OFL-*.txt`**。

字型來源檔與內嵌腳本住在 `fonts/`。改動字型設定後重新產生內嵌區塊：

```sh
python3 fonts/build-fonts.py          # 用本機 .woff2 重建頁面
python3 fonts/build-fonts.py --fetch  # 先重新下載字型再重建
```

腳本只會覆寫每個頁面裡 `<!-- fonts:begin -->` 到 `<!-- fonts:end -->` 之間的內容。
