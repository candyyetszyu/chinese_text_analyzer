# Chinese Text Analyzer

一個中文文本分析工具，適用於語言研究、內容分析和文本挖掘。

## 簡介

Chinese Text Analyzer 是一個用 Python 開發的中文文本分析工具，提供詞頻統計、詞性分析、命名實體識別、情感分析等功能，並支援繁簡體中文轉換和視覺化結果展示。

## 目錄

- [簡介](#簡介)
- [專案結構](#專案結構)
- [使用方式](#使用方式)
  - [互動式菜單介面（推薦）](#互動式菜單介面推薦)
  - [命令行界面](#命令行界面)
- [主要功能](#主要功能)
  - [核心分析功能](#核心分析功能)
  - [繁簡體轉換](#繁簡體轉換)
  - [視覺化功能](#視覺化功能)
    - [進階詞頻視覺化](#進階詞頻視覺化)
  - [圖像解析度設置](#圖像解析度設置)
- [文本處理能力](#文本處理能力)
  - [處理時間估算](#處理時間估算)
  - [加速處理方法](#加速處理方法)
- [環境設置](#環境設置)
  - [必要依賴](#必要依賴)
  - [使用虛擬環境（推薦）](#使用虛擬環境推薦)
- [中文字體配置](#中文字體配置)
  - [macOS中文字體問題解決方案](#macos中文字體問題解決方案)
    - [使用菜單界面自動檢測系統字體](#使用菜單界面自動檢測系統字體)
    - [手動指定字體](#手動指定字體)
    - [使用字體配置工具](#使用字體配置工具)
- [預設資源](#預設資源)
  - [停用詞和自定義詞典](#停用詞和自定義詞典)
  - [情感詞典](#情感詞典)
  - [標籤映射文件](#標籤映射文件)
- [API 使用指南](#api-使用指南)
  - [入門指南（適合編程初學者）](#入門指南適合編程初學者)
  - [常見問題與解決方案](#常見問題與解決方案)
  - [進階API示例（適合有編程經驗的用戶）](#進階api示例適合有編程經驗的用戶)
- [命令行參數參考](#命令行參數參考)
  - [基礎參數（適合初學者）](#基礎參數適合初學者)
  - [給初學者的命令行指南](#給初學者的命令行指南)
  - [命令行使用技巧](#命令行使用技巧)
  - [進階參數（適合熟悉命令行的用戶）](#進階參數適合熟悉命令行的用戶)
  - [常見命令行組合範例](#常見命令行組合範例)
- [未來擴展建議](#未來擴展建議)
  - [內容分析擴展](#內容分析擴展)
  - [技術改進](#技術改進)
  - [用戶界面優化](#用戶界面優化)
  - [集成與擴展性](#集成與擴展性)
- [鳴謝](#鳴謝)

## 專案結構

```
chinese_text_analyzer/
├── analyzer.py        # 核心分析功能實現
├── file_utils.py      # 文件操作工具類
├── main.py            # 命令行界面和主程序入口
├── menu.py            # 互動式菜單介面
├── visualization.py   # 數據視覺化功能
├── setup_chinese_font.py  # 中文字體配置工具
├── convert_chinese.py # 繁簡體中文轉換工具
├── convert_to_traditional.py # 簡體轉繁體工具（備用）
├── README.md          # 專案說明文檔
├── resources/         # 預設資源目錄
│   ├── chinese_stopwords.txt  # 中文停用詞表
│   ├── custom_dict.txt        # 自定義詞典
│   ├── positive_words.txt     # 正面情感詞典
│   ├── negative_words.txt     # 負面情感詞典
│   └── mappings/              # 詞性和實體映射文件
│       ├── pos_mapping.json   # 詞性映射
│       ├── entity_mapping.json # 實體類型映射
│       └── sentiment_mapping.json # 情感標籤映射
├── input_texts/       # 輸入文本文件目錄
└── results/           # 分析結果輸出目錄
    └── visualizations/      # 視覺化圖表目錄
        └── advanced/        # 進階詞頻視覺化目錄
```

## 使用方式

### 互動式菜單介面（推薦）

本工具提供了一個方便的互動式菜單介面，適合不熟悉命令行參數的用戶：

```bash
python menu.py
```

啟動後，您將看到以下主菜單：

```
=== 中文文本分析工具 ===
版本：1.0.0
=========================

主菜單:
1. 分析單個文件
2. 批量分析文件
3. 繁簡體轉換
4. 設置選項
5. 查看當前設置
0. 退出程序
```

主要功能菜單：
- **分析單個文件**：對選定的中文文本進行全面分析
- **批量分析文件**：一次處理多個文本文件
- **繁簡體轉換**：進行繁簡體中文轉換（支持文本和文件）
- **設置選項**：調整分析工具的各種參數
- **查看當前設置**：顯示目前的配置參數

進階選項設置包括：
- 輸出目錄和格式設定（支持JSON、CSV、Excel）
- 視覺化圖表控制
- 圖像解析度（DPI）調整
- 中文字體設置（自動檢測系統字體）
- 自定義詞典和停用詞表配置

### 命令行界面

除了菜單介面外，本工具也保留了完整的命令行界面，適合進階用戶或批處理需求：

```bash
python main.py --input input_texts/sample.txt --output results
```

## 主要功能

### 核心分析功能

- **詞頻分析**：統計文本中各詞語出現的頻率
- **詞性分析**：分析文本中不同詞性的分佈
- **命名實體識別**：識別文本中的人名、地名、機構名等
- **情感分析**：分析文本的情感傾向（正面、負面或中性）
- **關鍵詞提取**：基於 TF-IDF 算法提取文本關鍵詞
- **文本摘要**：自動生成文本摘要
- **N-gram分析**：識別文本中的常見詞組

### 繁簡體轉換

本工具提供完整的繁簡體中文轉換功能：

- **互動式轉換**：通過菜單界面直接轉換文本或文件
- **文本轉換**：直接在界面中輸入文本並轉換
- **文件轉換**：轉換整個文件，支持多種格式
- **批量轉換**：支持批量處理整個目錄中的文件
- **雙向轉換**：支持簡體→繁體和繁體→簡體轉換

通過命令行使用繁簡體轉換工具：

```bash
# 將單個文件從簡體轉為繁體
python convert_chinese.py --file your_file.txt

# 將單個文件從繁體轉為簡體
python convert_chinese.py --file your_file.txt --t2s

# 轉換整個目錄中的特定類型文件
python convert_chinese.py --dir your_folder --ext .txt,.md
```

### 視覺化功能

本工具生成多種視覺化圖表，幫助直觀理解文本分析結果：

- **詞頻統計圖**：展示詞語使用頻率
- **詞雲圖**：以視覺化方式展示高頻詞
- **詞性分布圖**：分析詞性結構
- **情感分析圖**：展示文本情感傾向
- **命名實體統計圖**：統計不同類型的命名實體
- **關鍵詞權重圖**：展示關鍵詞的重要性
- **N-gram頻率圖**：展示常見詞組

#### 進階詞頻視覺化

本工具還提供多種進階詞頻視覺化選項：

- **詞頻分布餅圖**：展示詞語分布比例
- **詞頻垂直條形圖**：比標準水平條形圖更適合某些分析場景
- **按詞長度排序的詞頻圖**：展示不同長度詞語的使用頻率

### 圖像解析度設置

使用菜單界面或命令行參數可以調整視覺化圖表的解析度（DPI），以平衡生成速度和圖像質量：

- **300 DPI**：高質量（默認）
- **150 DPI**：一般用途
- **72 DPI**：快速預覽

設置DPI值可以顯著影響處理大量文件時的性能：

```bash
# 命令行中設置DPI
python main.py --input sample.txt --output results --dpi 150

# 在菜單界面中設置
4. 設置選項 > 4. 設置圖像解析度 (DPI)
```

## 文本處理能力

本工具可處理各種規模的中文文本，從短句到長篇文章。處理效率取決於系統配置和文本規模。

### 處理時間估算

| 文本大小 | 估計處理時間 |
| --- | --- |
| 小型文本（1-5 KB，約 500-2,500 字） | 5-10 秒 |
| 中型文本（10-50 KB，約 5,000-25,000 字） | 20-60 秒 |
| 大型文本（100-500 KB，約 50,000-250,000 字） | 2-5 分鐘 |
| 超大型文本（1MB+ ，超過 500,000 字） | 10+ 分鐘 |

### 加速處理方法

提高處理效率的方法：

1. **使用並行處理**：適用於批量處理多個文件
   ```bash
   # 命令行中啟用並行處理
   python main.py --input input_folder --batch --parallel
   
   # 在菜單界面中啟用
   2. 批量分析文件 > 是否使用並行處理 > y
   ```

2. **調低視覺化解析度**：降低DPI值可大幅縮短處理時間
   ```bash
   # 使用低分辨率模式以加快渲染
   python main.py --input sample.txt --dpi 72
   ```

3. **關閉不必要的視覺化**：選擇性生成視覺化圖表
   ```bash
   # 只生成詞雲和詞頻統計圖
   python main.py --input sample.txt --viz word_frequency,wordcloud
   
   # 在菜單界面中
   4. 設置選項 > 3. 設置視覺化選項
   ```

## 環境設置

### 必要依賴

運行此工具需要以下 Python 庫：

```bash
pip install jieba pandas matplotlib seaborn wordcloud xlsxwriter opencc-python-reimplemented chardet
```

### 使用虛擬環境（推薦）

為避免依賴衝突，建議使用虛擬環境：

```bash
# 創建並啟動虛擬環境
python -m venv venv
source venv/bin/activate  # macOS/Linux
# venv\Scripts\activate   # Windows

# 安裝依賴
pip install jieba pandas matplotlib seaborn wordcloud xlsxwriter opencc-python-reimplemented chardet
```

## 中文字體配置

### macOS中文字體問題解決方案

在 macOS 上使用 matplotlib 顯示中文時可能遇到字體問題。本工具提供多種解決方案：

#### 使用菜單界面自動檢測系統字體

菜單界面會自動檢測macOS系統上的常見中文字體，並提供選擇：

```
4. 設置選項 > 5. 設置中文字體
```

#### 手動指定字體

指定字體路徑：

```bash
# 命令行界面
python main.py --input sample.txt --font /System/Library/Fonts/PingFang.ttc

# 或使用菜單界面手動輸入路徑
```

常見的 macOS 中文字體路徑：
- `/System/Library/Fonts/PingFang.ttc`
- `/System/Library/Fonts/STHeiti Light.ttc`
- `/System/Library/Fonts/STHeiti Medium.ttc`
- `/System/Library/Fonts/Hiragino Sans GB.ttc`
- `/System/Library/Fonts/Songti.ttc`

#### 使用字體配置工具

```bash
python setup_chinese_font.py
```

## 預設資源

本工具內置多種資源文件，優化分析效果：

### 停用詞和自定義詞典

- **停用詞表**：過濾常見但無意義的詞（代詞、助詞、連詞等）
- **自定義詞典**：包含專業術語、實體名稱、常見複合詞等

### 情感詞典

- **正面情感詞典**：包含各類正面情感詞
- **負面情感詞典**：包含各類負面情感詞

### 標籤映射文件

JSON格式的映射文件用於將技術代碼轉換為更易讀的中文標籤：

- **詞性映射**：將簡短詞性代碼轉換為中文詞性名稱
- **實體類型映射**：將英文實體類型轉換為中文標籤
- **情感標籤映射**：將情感分析結果轉換為中文情感標籤

## API 使用指南

除了互動式菜單和命令行界面，您也可以在Python程式中直接使用本工具的API。以下是適合初學者的基礎指南：

### 入門指南（適合編程初學者）

如果您不熟悉編程，但希望嘗試使用本工具的API，請按照以下步驟操作：

1. **建立一個新的Python文件**：
   - 在文字編輯器中新建文件（例如 `my_analysis.py`）
   - 確保文件與 Chinese Text Analyzer 工具在同一目錄下

2. **複製基本範例**：將以下基本範例複製到您的文件中

```python
# 導入必要的庫（這些是本工具的核心元件）
from analyzer import ChineseTextAnalyzer
from visualization import Visualizer

# 初始化分析器（必須的第一步）
analyzer = ChineseTextAnalyzer()

# 您要分析的文本（替換為您自己的文本）
text = "這是一段示例中文文本，用於展示分析功能。"

# 進行全面分析
results = analyzer.analyze_text(text)

# 顯示基本分析結果
print("詞頻分析結果:")
for word, freq in list(results['word_frequency'].items())[:5]:
    print(f"  {word}: {freq} 次")

print("\n詞性分析結果:")
for pos, count in list(results['pos_distribution'].items())[:3]:
    print(f"  {pos}: {count} 個詞")

# 生成詞雲圖（最直觀的視覺化效果）
Visualizer.generate_wordcloud(
    results['word_frequency'], 
    title='我的第一個詞雲',
    output_file='my_first_wordcloud.png'
)

print("\n分析完成！詞雲圖已保存為 'my_first_wordcloud.png'")
```

3. **運行您的程式**：
   - 打開終端或命令提示符
   - 進入到您的工作目錄
   - 執行 `python my_analysis.py`

### 常見問題與解決方案

- **找不到模塊錯誤**：確保您在正確的目錄中執行程式
- **中文顯示為亂碼**：尝试添加 `font_path='/System/Library/Fonts/PingFang.ttc'` 參數到 `generate_wordcloud` 函數中
- **程序執行緩慢**：對於較長文本，降低 DPI 值可提高速度（例如：`dpi=150`）

### 進階API示例（適合有編程經驗的用戶）

以下是更多進階API用法示例，供有一定編程經驗的用戶參考：

```python
from analyzer import ChineseTextAnalyzer
from visualization import Visualizer

# 初始化分析器
analyzer = ChineseTextAnalyzer()

# 分析文本
text = "這是一段示例中文文本，用於展示分析功能。"
results = analyzer.analyze_text(text)

# 進行情感分析
sentiment = analyzer.analyze_sentiment(text)
print(f"情感分析結果: {sentiment['sentiment_label']}")

# 提取關鍵詞
keywords = analyzer.keyword_extraction(text, top_k=5)
print(f"前五個關鍵詞: {list(keywords.keys())}")

# 生成詞雲圖
Visualizer.generate_wordcloud(
    results['word_frequency'], 
    title='自定義詞雲標題',
    figsize=(12, 10),
    background_color='black',
    max_words=100,
    font_path='/System/Library/Fonts/PingFang.ttc'  # macOS中文字體路徑
)

# 生成完整視覺化報告
viz_dir = Visualizer.create_visualization_report(
    results,
    output_dir='my_visualizations',
    prefix='custom_',
    font_path='/System/Library/Fonts/PingFang.ttc',
    dpi=300
)

# 使用進階詞頻視覺化API
Visualizer.plot_advanced_word_frequency(
    results['word_frequency'],
    top_n=15,
    title='詞頻分布餅圖',
    save_path='my_visualizations/word_freq_pie.png',
    plot_type='pie',
    dpi=300
)
```

## 命令行參數參考

以下是所有可用的命令行參數說明，包括基本用法範例：

### 基礎參數（適合初學者）

| 參數 | 簡寫 | 描述 | 範例 |
| --- | --- | --- | --- |
| `--input` | `-i` | 輸入文件或目錄路徑 | `--input sample.txt` |
| `--output` | `-o` | 輸出目錄路徑（預設：results） | `--output my_results` |
| `--no-viz` | | 不生成視覺化圖表 | `--no-viz` |
| `--dpi` | | 視覺化分辨率（預設：300） | `--dpi 150` |
| `--font` | | 中文字體路徑 | `--font /System/Library/Fonts/PingFang.ttc` |

### 給初學者的命令行指南

如果您不熟悉命令行操作，以下是一個逐步指南：

1. **開啟終端或命令提示符**：
   - macOS：按下 `Command+空格` 鍵，輸入「Terminal」並按回車
   - Windows：按下 `Win+R` 鍵，輸入「cmd」並按回車

2. **導航到程式目錄**：
   ```
   cd 程式所在的路徑
   ```
   例如：`cd Downloads/chinese_text_analyzer`

3. **執行基本分析**：
   ```
   python main.py --input input_texts/sample.txt
   ```
   這會分析 `input_texts` 資料夾中的 `sample.txt` 文件

4. **範例：自定義輸出目錄**：
   ```
   python main.py --input input_texts/sample.txt --output my_results
   ```
   這會將分析結果保存到 `my_results` 目錄

5. **範例：設置低分辨率以加快處理**：
   ```
   python main.py --input input_texts/sample.txt --dpi 72
   ```
   這會以低分辨率生成視覺化圖表，適合快速預覽

### 命令行使用技巧

- **組合多個參數**：您可以同時使用多個參數
  ```
  python main.py --input sample.txt --output custom_results --dpi 150 --font /System/Library/Fonts/PingFang.ttc
  ```

- **使用簡寫形式**：大多數參數都有簡寫形式，可使命令更簡潔
  ```
  python main.py -i sample.txt -o custom_results
  ```

- **批量處理文件**：使用 `--batch` 參數處理整個目錄
  ```
  python main.py --input input_folder --batch
  ```

### 進階參數（適合熟悉命令行的用戶）

| 參數 | 簡寫 | 描述 | 範例 |
| --- | --- | --- | --- |
| `--dict` | `-d` | 自定義詞典路徑 | `--dict my_dict.txt` |
| `--stopwords` | `-s` | 停用詞表路徑 | `--stopwords my_stopwords.txt` |
| `--formats` | `-f` | 輸出格式，多種格式用逗號分隔 | `--formats json,csv,excel` |
| `--batch` | `-b` | 批量處理模式（處理整個目錄） | `--batch` |
| `--parallel` | `-p` | 使用並行處理（加速批量處理） | `--parallel` |
| `--extensions` | `-e` | 要處理的文件擴展名（批量模式） | `--extensions .txt,.md` |
| `--debug` | | 啟用調試模式（顯示更多技術訊息） | `--debug` |
| `--advanced-viz` | `-av` | 進階詞頻視覺化選項 | `--advanced-viz pie,vertical,length` |
| `--viz` | `-v` | 指定要生成的視覺化圖表類型 | `--viz wordcloud,word_frequency` |

### 常見命令行組合範例

```bash
# 基本分析
python main.py --input sample.txt

# 使用自定義字體和輸出目錄
python main.py --input sample.txt --output my_results --font /System/Library/Fonts/PingFang.ttc

# 批量處理目錄中所有.txt文件，使用並行加速
python main.py --input input_folder --batch --extensions .txt --parallel

# 生成所有格式的數據，但不生成視覺化圖表（快速處理）
python main.py --input sample.txt --formats json,csv,excel --no-viz

# 只生成詞雲和詞頻圖，使用低分辨率
python main.py --input sample.txt --viz wordcloud,word_frequency --dpi 72

# 使用進階視覺化選項
python main.py --input sample.txt --advanced-viz pie,vertical,length
```

## 未來擴展建議

如想進一步發展，我建議未來版本可考慮添加以下功能和改進：

### 內容分析擴展

- **主題建模**：整合 LDA（Latent Dirichlet Allocation）主題建模，自動發現文本中的主題結構
- **文本相似度比較**：添加多文本相似度分析，比較不同文本之間的關聯性
- **時間序列分析**：針對具有時間戳記的文本集合，提供語言使用隨時間變化的趨勢分析
- **關聯詞分析**：探索詞語之間的關聯及共現關係，提供更深入的語義理解

### 用戶界面優化

- **網頁界面**：開發基於瀏覽器的網頁界面，無需命令行或本地安裝
- **更多視覺化選項**：提供更豐富的交互式視覺化選項（如熱力圖、網絡圖等）
- **批量任務隊列**：實現任務隊列系統，更好地管理大批量處理任務
- **實時分析儀表板**：提供實時文本分析儀表板，動態展示分析結果

### 技術改進

- **GPU 加速支持**：對於大型文本處理提供 GPU 加速選項
- **更多文本格式支持**：擴展 PDF、Word、網頁等格式的直接解析能力
- **機器學習增強**：整合更先進的機器學習模型提升情感分析和關鍵詞提取的準確性

### 集成與擴展性

- **API擴展**：提供完整的 RESTful API，便於與其他系統集成
- **插件系統**：開發插件架構，允許社區成員貢獻新功能和擴展
- **數據庫集成**：添加與常見數據庫系統的連接器，便於大規模文本處理

## 鳴謝
此程式由Claude 3.7 Sonnet及Deepseek協助完成。