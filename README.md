# Chinese Text Analyzer

一個功能強大的中文文本分析工具，適用於語言研究、內容分析和文本挖掘。

## 簡介

Chinese Text Analyzer 是一個用 Python 開發的中文文本分析工具，提供詞頻統計、詞性分析、命名實體識別、情感分析等功能，並支援繁簡體中文轉換和視覺化結果展示。

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

菜單介面的優點：
- 無需記憶複雜的命令行參數
- 直觀的設置選項，包括輸出格式、視覺化選項等
- 方便的中文字體設置（特別是在 macOS 上）
- 即時顯示分析進度和結果
- 集成了繁簡體中文轉換功能

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

除了互動式菜單和命令行界面，您也可以在Python程式中直接使用本工具的API：

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

| 參數 | 簡寫 | 描述 |
| --- | --- | --- |
| `--input` | `-i` | 輸入文件或目錄路徑 |
| `--output` | `-o` | 輸出目錄路徑（預設：results） |
| `--dict` | `-d` | 自定義詞典路徑 |
| `--stopwords` | `-s` | 停用詞表路徑 |
| `--formats` | `-f` | 輸出格式（預設：json，可選：csv,excel） |
| `--no-viz` | | 不生成視覺化圖表 |
| `--batch` | `-b` | 批量處理模式 |
| `--parallel` | `-p` | 使用並行處理 |
| `--extensions` | `-e` | 要處理的文件擴展名（批量模式） |
| `--font` | | 中文字體路徑 |
| `--dpi` | | 視覺化分辨率（預設：300） |
| `--debug` | | 啟用調試模式 |
| `--advanced-viz` | `-av` | 進階詞頻視覺化選項（例如：pie,vertical,length）|

## 鳴謝
此程式由Claude 3.7 Sonnet及Deepseek協助完成。