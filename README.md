# Chinese Text Analyzer

一個功能強大的中文文本分析工具，適用於語言研究、內容分析和文本挖掘。

## 簡介

Chinese Text Analyzer 是一個用 Python 開發的中文文本分析工具，提供詞頻統計、詞性分析、命名實體識別、情感分析等功能，並支援繁簡體中文轉換和視覺化結果展示。

## 專案結構

```
chinese_text_analyzer/
├── analyzer.py        # 核心分析功能實現
├── file_utils.py      # 文件操作工具類
├── main.py            # 命令行界面和主程序入口
├── visualization.py   # 數據視覺化功能
├── setup_chinese_font.py  # 中文字體配置工具
├── convert_chinese.py # 繁簡體中文轉換工具
├── README.md          # 專案說明文檔
├── resources/         # 預設資源目錄
│   ├── chinese_stopwords.txt  # 中文停用詞表
│   ├── custom_dict.txt        # 自定義詞典
│   ├── positive_words.txt     # 正面情感詞典
│   └── negative_words.txt     # 負面情感詞典
├── input_texts/       # 輸入文本文件目錄
└── results/           # 分析結果輸出目錄
```

## 文本處理能力

本工具對於可分析的文本大小沒有明確限制，可處理從短句到長篇文章的各種中文文本。處理效率取決於系統配置和文本規模。對於特別大的文件（數百萬字以上），建議使用 `--parallel` 參數啟用並行處理模式以提高效率。

## 環境設置

### 使用虛擬環境（推薦）

為避免依賴衝突，建議使用虛擬環境運行此項目：

```bash
# 創建並啟動虛擬環境
python -m venv venv
source venv/bin/activate  # macOS/Linux
# venv\Scripts\activate   # Windows

# 安裝依賴
pip install -r requirements.txt
```

如果您還沒有 requirements.txt 文件，可以安裝以下依賴：

```bash
pip install jieba pandas matplotlib seaborn wordcloud xlsxwriter opencc-python-reimplemented chardet
```

## 快速開始

### 基本用法

分析單個文件：

```bash
python main.py --input input_texts/sample.txt --output results
```

此命令會生成分析結果並保存到 `results` 目錄，包括文字分析結果和視覺化圖表。

## 主要功能

- **詞頻分析**：統計文本中各詞語出現的頻率
- **詞性分析**：分析文本中不同詞性的分佈
- **命名實體識別**：識別文本中的人名、地名、機構名等
- **情感分析**：分析文本的情感傾向（正面、負面或中性）
- **關鍵詞提取**：基於 TF-IDF 算法提取文本關鍵詞
- **文本摘要**：自動生成文本摘要
- **繁簡體轉換**：支持繁體中文和簡體中文的相互轉換
- **N-gram分析**：識別文本中的常見詞組

## 預設資源

本工具提供了多種預設資源文件，自動優化文本分析效果：

### 停用詞表

預設的中文停用詞表 (`resources/chinese_stopwords.txt`) 包含常見的功能詞，如：

- 代詞 (我, 你, 他, 她, 它, 們)
- 助詞 (的, 地, 得, 了, 著)
- 連詞 (和, 與, 而, 但)
- 介詞 (在, 於, 從, 對)
- 常用動詞 (是, 有, 來, 去, 說)
- 指示詞 (這, 那, 些)

### 情感詞典

預設的情感詞典用於提高情感分析準確度：

- 正面情感詞典 (`resources/positive_words.txt`)：包含 50+ 正面情感詞
- 負面情感詞典 (`resources/negative_words.txt`)：包含 50+ 負面情感詞

### 自定義詞典

預設的自定義詞典 (`resources/custom_dict.txt`) 包含多種專業術語和實體名稱，包括：

- 人名 (政治人物, 科技領袖)
- 地名 (主要中國城市及地區)
- 機構名 (主要中國科技公司)
- 專業術語 (人工智能, 機器學習, 區塊鏈等)
- 網路用語 (流行網絡術語)

## 進階用法

### 批量處理多個文件

```bash
python main.py --input input_folder --output results --batch
```

### 指定輸出格式

```bash
python main.py --input sample.txt --output results --formats json,csv,excel
```

### 自定義詞典和停用詞

您可以使用自定義詞典來提高分詞準確性，並使用停用詞表過濾不需要的詞語：

```bash
python main.py --input sample.txt --dict custom_dict.txt --stopwords stopwords.txt
```

自定義詞典格式範例：
```
詞語 詞頻 詞性
人工智能 100 n
機器學習 80 n
深度學習 60 n
```

停用詞格式範例（每行一個詞）：
```
的
了
和
```

也可以在程式中設置：

```python
analyzer = ChineseTextAnalyzer()
analyzer.load_stopwords('path/to/stopwords.txt')
analyzer.load_user_dict('path/to/custom_dict.txt')
```

### 加速大規模文本處理

```bash
python main.py --input large_corpus --batch --parallel
```

### 選擇性生成視覺化圖表

```bash
# 只生成詞雲和詞頻統計圖
python main.py --input sample.txt --viz word_frequency,wordcloud
```

可用的視覺化類型：
- `word_frequency` - 詞頻統計圖
- `wordcloud` - 詞雲圖
- `pos_distribution` - 詞性分布圖
- `sentiment` - 情感分析圖
- `ngrams` - 詞組頻率圖
- `entities` - 命名實體統計圖
- `keywords` - 關鍵詞權重圖

## 中文字體配置

### macOS中文字體問題解決方案

在 macOS 上使用 matplotlib 顯示中文可能會遇到字體問題。本工具提供多種解決方案：

#### 自動配置中文字體

```bash
# 運行字體配置工具
python setup_chinese_font.py
```

此工具會自動檢測系統中可用的中文字體，並配置 matplotlib 使用最合適的字體。

#### 手動指定字體

您也可以直接指定字體路徑：

```bash
python main.py --input sample.txt --font /System/Library/Fonts/PingFang.ttc
```

常見的 macOS 中文字體路徑：
- `/System/Library/Fonts/PingFang.ttc`
- `/System/Library/Fonts/STHeiti Light.ttc`
- `/System/Library/Fonts/STHeiti Medium.ttc`
- `/System/Library/Fonts/Hiragino Sans GB.ttc`
- `/System/Library/Fonts/Songti.ttc`

#### 查看系統可用中文字體

```bash
python -c "import matplotlib.font_manager as fm; print('\n'.join([f for f in fm.findSystemFonts() if any(k in f.lower() for k in ['ping', 'hei', 'song', 'ming'])]))"
```

## 繁簡體轉換工具

### 轉換單個文件

```bash
python convert_chinese.py --file your_file.py
```

### 轉換整個目錄

```bash
python convert_chinese.py --dir . --ext .py
```

### 遞歸轉換整個項目

```bash
python convert_chinese.py --dir . --recursive
```

顯示更多選項：

```bash
python convert_chinese.py --help
```

## 使用API進行自定義分析

除了命令行界面外，您也可以將此工具作為程式庫在您的 Python 專案中使用：

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
    font_path='/System/Library/Fonts/PingFang.ttc'
)
```

## 命令行參數參考

| 參數 | 簡寫 | 描述 |
| --- | --- | --- |
| `--input` | `-i` | 輸入文件或目錄路徑 |
| `--output` | `-o` | 輸出目錄路徑（預設：results） |
| `--dict` | `-d` | 自定義詞典路徑 |
| `--stopwords` | `-s` | 停用詞表路徑 |
| `--formats` | `-f` | 輸出格式（預設：json） |
| `--viz` | `-v` | 視覺化類型（例如：wordcloud,sentiment） |
| `--batch` | `-b` | 批量處理模式 |
| `--parallel` | `-p` | 使用並行處理 |
| `--font` | | 中文字體路徑 |
| `--debug` | | 啟用調試模式 |