# Chinese Text Analyzer

A Chinese text analysis tool for language research, content analysis, and text mining.

## Introduction

Chinese Text Analyzer is a Python-based Chinese text analysis tool that provides word frequency statistics, part-of-speech analysis, named entity recognition, sentiment analysis, and other features. It supports Simplified and Traditional Chinese conversion and visualization of results.

## Table of Contents

- [Introduction](#introduction)
- [Project Structure](#project-structure)
- [Usage](#usage)
  - [Interactive Menu Interface (Recommended)](#interactive-menu-interface-recommended)
  - [Command Line Interface](#command-line-interface)
- [Main Features](#main-features)
  - [Core Analysis Features](#core-analysis-features)
  - [Traditional and Simplified Chinese Conversion](#traditional-and-simplified-chinese-conversion)
  - [Visualization Features](#visualization-features)
    - [Advanced Word Frequency Visualization](#advanced-word-frequency-visualization)
  - [Image Resolution Settings](#image-resolution-settings)
- [Text Processing Capabilities](#text-processing-capabilities)
  - [Processing Time Estimation](#processing-time-estimation)
  - [Methods to Accelerate Processing](#methods-to-accelerate-processing)
- [Environment Setup](#environment-setup)
  - [Required Dependencies](#required-dependencies)
  - [Using Virtual Environment (Recommended)](#using-virtual-environment-recommended)
- [Chinese Font Configuration](#chinese-font-configuration)
  - [macOS Chinese Font Issue Solutions](#macos-chinese-font-issue-solutions)
    - [Using Menu Interface for Automatic System Font Detection](#using-menu-interface-for-automatic-system-font-detection)
    - [Manual Font Specification](#manual-font-specification)
    - [Using Font Configuration Tool](#using-font-configuration-tool)
- [Default Resources](#default-resources)
  - [Stopwords and Custom Dictionary](#stopwords-and-custom-dictionary)
  - [Sentiment Dictionary](#sentiment-dictionary)
  - [Tag Mapping Files](#tag-mapping-files)
- [API Usage Guide](#api-usage-guide)
  - [Getting Started Guide (For Programming Beginners)](#getting-started-guide-for-programming-beginners)
  - [Common Issues and Solutions](#common-issues-and-solutions)
  - [Advanced API Examples (For Experienced Users)](#advanced-api-examples-for-experienced-users)
- [Command Line Parameter Reference](#command-line-parameter-reference)
  - [Basic Parameters (For Beginners)](#basic-parameters-for-beginners)
  - [Command Line Guide for Beginners](#command-line-guide-for-beginners)
  - [Command Line Usage Tips](#command-line-usage-tips)
  - [Advanced Parameters (For Command Line Experienced Users)](#advanced-parameters-for-command-line-experienced-users)
  - [Common Command Line Combination Examples](#common-command-line-combination-examples)
- [Future Enhancement Suggestions](#future-enhancement-suggestions)
  - [Content Analysis Extensions](#content-analysis-extensions)
  - [Technical Improvements](#technical-improvements)
  - [User Interface Optimization](#user-interface-optimization)
  - [Integration and Extensibility](#integration-and-extensibility)
- [Acknowledgments](#acknowledgments)

## Project Structure

```
chinese_text_analyzer/
├── analyzer.py        # Core analysis functionality implementation
├── file_utils.py      # File operation utility class
├── main.py            # Command line interface and main program entry
├── menu.py            # Interactive menu interface
├── visualization.py   # Data visualization functionality
├── setup_chinese_font.py  # Chinese font configuration tool
├── convert_chinese.py # Traditional/Simplified Chinese conversion tool
├── convert_to_traditional.py # Simplified to Traditional conversion tool (backup)
├── README.md          # Project documentation
├── resources/         # Default resources directory
│   ├── chinese_stopwords.txt  # Chinese stopwords list
│   ├── custom_dict.txt        # Custom dictionary
│   ├── positive_words.txt     # Positive sentiment dictionary
│   ├── negative_words.txt     # Negative sentiment dictionary
│   └── mappings/              # POS and entity mapping files
│       ├── pos_mapping.json   # Part-of-speech mapping
│       ├── entity_mapping.json # Entity type mapping
│       └── sentiment_mapping.json # Sentiment label mapping
├── input_texts/       # Input text files directory
└── results/           # Analysis results output directory
    └── visualizations/      # Visualization charts directory
        └── advanced/        # Advanced word frequency visualization directory
```

## Usage

### Interactive Menu Interface (Recommended)

This tool provides a convenient interactive menu interface suitable for users unfamiliar with command line parameters:

```bash
python menu.py
```

After startup, you will see the following main menu:

```
=== Chinese Text Analysis Tool ===
Version: 1.0.0
=================================

Main Menu:
1. Analyze single file
2. Batch analyze files
3. Traditional/Simplified Chinese conversion
4. Settings options
5. View current settings
0. Exit program
```

Main feature menu:
- **Analyze single file**: Comprehensive analysis of selected Chinese text
- **Batch analyze files**: Process multiple text files at once
- **Traditional/Simplified Chinese conversion**: Convert between Traditional and Simplified Chinese (supports text and files)
- **Settings options**: Adjust various parameters of the analysis tool
- **View current settings**: Display current configuration parameters

Advanced option settings include:
- Output directory and format settings (supports JSON, CSV, Excel)
- Visualization chart control
- Image resolution (DPI) adjustment
- Chinese font settings (automatic system font detection)
- Custom dictionary and stopwords list configuration

### Command Line Interface

In addition to the menu interface, this tool also retains a complete command line interface, suitable for advanced users or batch processing needs:

```bash
python main.py --input input_texts/sample.txt --output results
```

## Main Features

### Core Analysis Features

- **Word Frequency Analysis**: Statistics of word occurrence frequency in text
- **Part-of-Speech Analysis**: Analysis of the distribution of different parts of speech in text
- **Named Entity Recognition**: Identification of person names, place names, organization names, etc. in text
- **Sentiment Analysis**: Analysis of text sentiment tendency (positive, negative, or neutral)
- **Keyword Extraction**: Extract text keywords based on TF-IDF algorithm
- **Text Summarization**: Automatically generate text summaries
- **N-gram Analysis**: Identify common phrases in text
- **Chinese Character Statistics**: Calculate the number and proportion of Chinese characters in text

### Traditional and Simplified Chinese Conversion

This tool provides complete Traditional and Simplified Chinese conversion functionality:

- **Interactive Conversion**: Direct text or file conversion through menu interface
- **Text Conversion**: Directly input text in the interface and convert
- **File Conversion**: Convert entire files, supporting multiple formats
- **Batch Conversion**: Support batch processing of files in entire directories
- **Bidirectional Conversion**: Support Simplified→Traditional and Traditional→Simplified conversion

Using Traditional/Simplified Chinese conversion tool through command line:

```bash
# Convert single file from Simplified to Traditional
python convert_chinese.py --file your_file.txt

# Convert single file from Traditional to Simplified
python convert_chinese.py --file your_file.txt --t2s

# Convert specific file types in entire directory
python convert_chinese.py --dir your_folder --ext .txt,.md
```

### Visualization Features

This tool generates various visualization charts to help intuitively understand text analysis results:

- **Word Frequency Charts**: Display word usage frequency
- **Word Clouds**: Visually display high-frequency words
- **Part-of-Speech Distribution Charts**: Analyze grammatical structure
- **Sentiment Analysis Charts**: Display text sentiment tendency
- **Named Entity Statistics Charts**: Statistics of different types of named entities
- **Keyword Weight Charts**: Display the importance of keywords
- **N-gram Frequency Charts**: Display common phrases

#### Advanced Word Frequency Visualization

This tool also provides various advanced word frequency visualization options:

- **Word Frequency Distribution Pie Chart**: Display word distribution proportions
- **Word Frequency Vertical Bar Chart**: More suitable for certain analysis scenarios than standard horizontal bar charts
- **Word Frequency Chart Sorted by Word Length**: Display usage frequency of words of different lengths

### Image Resolution Settings

Using the menu interface or command line parameters can adjust the resolution (DPI) of visualization charts to balance generation speed and image quality:

- **300 DPI**: High quality (default)
- **150 DPI**: General purpose
- **72 DPI**: Quick preview

Setting DPI values can significantly affect performance when processing large numbers of files:

```bash
# Set DPI in command line
python main.py --input sample.txt --output results --dpi 150

# Set in menu interface
4. Settings Options > 4. Set Image Resolution (DPI)
```

## Text Processing Capabilities

This tool can process Chinese texts of various scales, from short sentences to long articles. Processing efficiency depends on system configuration and text scale.

### Processing Time Estimation

| Text Size | Estimated Processing Time |
| --- | --- |
| Small text (1-5 KB, about 500-2,500 characters) | 5-10 seconds |
| Medium text (10-50 KB, about 5,000-25,000 characters) | 20-60 seconds |
| Large text (100-500 KB, about 50,000-250,000 characters) | 2-5 minutes |
| Extra large text (1MB+, over 500,000 characters) | 10+ minutes |

### Methods to Accelerate Processing

Methods to improve processing efficiency:

1. **Use parallel processing**: Suitable for batch processing multiple files
   ```bash
   # Enable parallel processing in command line
   python main.py --input input_folder --batch --parallel
   
   # Enable in menu interface
   2. Batch analyze files > Use parallel processing? > y
   ```

2. **Lower visualization resolution**: Reducing DPI values can significantly shorten processing time
   ```bash
   # Use low resolution mode to speed up rendering
   python main.py --input sample.txt --dpi 72
   ```

3. **Turn off unnecessary visualizations**: Selectively generate visualization charts
   ```bash
   # Only generate word cloud and word frequency charts
   python main.py --input sample.txt --viz word_frequency,wordcloud
   
   # In menu interface
   4. Settings Options > 3. Set Visualization Options
   ```

## Environment Setup

### Required Dependencies

Running this tool requires the following Python libraries:

```bash
pip install jieba pandas matplotlib seaborn wordcloud xlsxwriter opencc-python-reimplemented chardet
```

### Using Virtual Environment (Recommended)

To avoid dependency conflicts, it is recommended to use a virtual environment:

```bash
# Create and activate virtual environment
python -m venv venv
source venv/bin/activate  # macOS/Linux
# venv\Scripts\activate   # Windows

# Install dependencies
pip install jieba pandas matplotlib seaborn wordcloud xlsxwriter opencc-python-reimplemented chardet
```

## Chinese Font Configuration

### macOS Chinese Font Issue Solutions

When using matplotlib to display Chinese on macOS, font issues may be encountered. This tool provides multiple solutions:

#### Using Menu Interface for Automatic System Font Detection

The menu interface will automatically detect common Chinese fonts on macOS systems and provide options:

```
4. Settings Options > 5. Set Chinese Font
```

#### Manual Font Specification

Specify font path:

```bash
# Command line interface
python main.py --input sample.txt --font /System/Library/Fonts/PingFang.ttc

# Or manually input path using menu interface
```

Common macOS Chinese font paths:
- `/System/Library/Fonts/PingFang.ttc`
- `/System/Library/Fonts/STHeiti Light.ttc`
- `/System/Library/Fonts/STHeiti Medium.ttc`
- `/System/Library/Fonts/Hiragino Sans GB.ttc`
- `/System/Library/Fonts/Songti.ttc`

#### Using Font Configuration Tool

```bash
python setup_chinese_font.py
```

## Default Resources

This tool includes various resource files to optimize analysis effectiveness:

### Stopwords and Custom Dictionary

- **Stopwords List**: Filter common but meaningless words (pronouns, particles, conjunctions, etc.)
- **Custom Dictionary**: Include specialized terms, entity names, common compound words, etc.

### Sentiment Dictionary

- **Positive Sentiment Dictionary**: Contains various positive sentiment words
- **Negative Sentiment Dictionary**: Contains various negative sentiment words

### Tag Mapping Files

JSON format mapping files are used to convert technical codes to more readable Chinese labels:

- **Part-of-Speech Mapping**: Convert short POS codes to Chinese part-of-speech names
- **Entity Type Mapping**: Convert English entity types to Chinese labels
- **Sentiment Label Mapping**: Convert sentiment analysis results to Chinese sentiment labels

## API Usage Guide

In addition to the interactive menu and command line interface, you can also directly use this tool's API in Python programs. The following is a basic guide suitable for beginners:

### Getting Started Guide (For Programming Beginners)

If you are not familiar with programming but want to try using this tool's API, please follow these steps:

1. **Create a new Python file**:
   - Create a new file in a text editor (e.g., `my_analysis.py`)
   - Ensure the file is in the same directory as the Chinese Text Analyzer tool

2. **Copy basic example**: Copy the following basic example to your file

```python
# Import necessary libraries (these are the core components of this tool)
from analyzer import ChineseTextAnalyzer
from visualization import Visualizer

# Initialize analyzer (required first step)
analyzer = ChineseTextAnalyzer()

# Text you want to analyze (replace with your own text)
text = "This is a sample Chinese text to demonstrate analysis functionality."

# Perform comprehensive analysis
results = analyzer.analyze_text(text)

# Display basic analysis results
print("Word frequency analysis results:")
for word, freq in list(results['word_frequency'].items())[:5]:
    print(f"  {word}: {freq} times")

print("\nPart-of-speech analysis results:")
for pos, count in list(results['pos_distribution'].items())[:3]:
    print(f"  {pos}: {count} words")

# Generate word cloud (most intuitive visualization effect)
Visualizer.generate_wordcloud(
    results['word_frequency'], 
    title='My First Word Cloud',
    output_file='my_first_wordcloud.png'
)

print("\nAnalysis complete! Word cloud saved as 'my_first_wordcloud.png'")
```

3. **Run your program**:
   - Open terminal or command prompt
   - Navigate to your working directory
   - Execute `python my_analysis.py`

### Common Issues and Solutions

- **Module not found error**: Ensure you are executing the program in the correct directory
- **Chinese characters display as garbled text**: Try adding `font_path='/System/Library/Fonts/PingFang.ttc'` parameter to the `generate_wordcloud` function
- **Program runs slowly**: For longer texts, lowering DPI values can improve speed (e.g., `dpi=150`)

### Advanced API Examples (For Experienced Users)

The following are more advanced API usage examples for users with programming experience:

```python
from analyzer import ChineseTextAnalyzer
from visualization import Visualizer

# Initialize analyzer
analyzer = ChineseTextAnalyzer()

# Analyze text
text = "This is a sample Chinese text to demonstrate analysis functionality."
results = analyzer.analyze_text(text)

# Perform sentiment analysis
sentiment = analyzer.analyze_sentiment(text)
print(f"Sentiment analysis result: {sentiment['sentiment_label']}")

# Extract keywords
keywords = analyzer.keyword_extraction(text, top_k=5)
print(f"Top five keywords: {list(keywords.keys())}")

# Generate word cloud
Visualizer.generate_wordcloud(
    results['word_frequency'], 
    title='Custom Word Cloud Title',
    figsize=(12, 10),
    background_color='black',
    max_words=100,
    font_path='/System/Library/Fonts/PingFang.ttc'  # macOS Chinese font path
)

# Generate complete visualization report
viz_dir = Visualizer.create_visualization_report(
    results,
    output_dir='my_visualizations',
    prefix='custom_',
    font_path='/System/Library/Fonts/PingFang.ttc',
    dpi=300
)

# Use advanced word frequency visualization API
Visualizer.plot_advanced_word_frequency(
    results['word_frequency'],
    top_n=15,
    title='Word Frequency Distribution Pie Chart',
    save_path='my_visualizations/word_freq_pie.png',
    plot_type='pie',
    dpi=300
)
```

## Command Line Parameter Reference

The following are descriptions of all available command line parameters, including basic usage examples:

### Basic Parameters (For Beginners)

| Parameter | Short | Description | Example |
| --- | --- | --- | --- |
| `--input` | `-i` | Input file or directory path | `--input sample.txt` |
| `--output` | `-o` | Output directory path (default: results) | `--output my_results` |
| `--no-viz` | | Do not generate visualization charts | `--no-viz` |
| `--dpi` | | Visualization resolution (default: 300) | `--dpi 150` |
| `--font` | | Chinese font path | `--font /System/Library/Fonts/PingFang.ttc` |

### Command Line Guide for Beginners

If you are not familiar with command line operations, here is a step-by-step guide:

1. **Open terminal or command prompt**:
   - macOS: Press `Command+Space`, type "Terminal" and press Enter
   - Windows: Press `Win+R`, type "cmd" and press Enter

2. **Navigate to program directory**:
   ```
   cd path_to_program
   ```
   For example: `cd Downloads/chinese_text_analyzer`

3. **Execute basic analysis**:
   ```
   python main.py --input input_texts/sample.txt
   ```
   This will analyze the `sample.txt` file in the `input_texts` folder

4. **Example: Custom output directory**:
   ```
   python main.py --input input_texts/sample.txt --output my_results
   ```
   This will save analysis results to the `my_results` directory

5. **Example: Set low resolution for faster processing**:
   ```
   python main.py --input input_texts/sample.txt --dpi 72
   ```
   This will generate visualization charts at low resolution, suitable for quick preview

### Command Line Usage Tips

- **Combine multiple parameters**: You can use multiple parameters simultaneously
  ```
  python main.py --input sample.txt --output custom_results --dpi 150 --font /System/Library/Fonts/PingFang.ttc
  ```

- **Use short forms**: Most parameters have short forms to make commands more concise
  ```
  python main.py -i sample.txt -o custom_results
  ```

- **Batch process files**: Use `--batch` parameter to process entire directories
  ```
  python main.py --input input_folder --batch
  ```

### Advanced Parameters (For Command Line Experienced Users)

| Parameter | Short | Description | Example |
| --- | --- | --- | --- |
| `--dict` | `-d` | Custom dictionary path | `--dict my_dict.txt` |
| `--stopwords` | `-s` | Stopwords list path | `--stopwords my_stopwords.txt` |
| `--formats` | `-f` | Output formats, multiple formats separated by commas | `--formats json,csv,excel` |
| `--batch` | `-b` | Batch processing mode (process entire directory) | `--batch` |
| `--parallel` | `-p` | Use parallel processing (accelerate batch processing) | `--parallel` |
| `--extensions` | `-e` | File extensions to process (batch mode) | `--extensions .txt,.md` |
| `--debug` | | Enable debug mode (show more technical information) | `--debug` |
| `--advanced-viz` | `-av` | Advanced word frequency visualization options | `--advanced-viz pie,vertical,length` |
| `--viz` | `-v` | Specify types of visualization charts to generate | `--viz wordcloud,word_frequency` |

### Common Command Line Combination Examples

```bash
# Basic analysis
python main.py --input sample.txt

# Use custom font and output directory
python main.py --input sample.txt --output my_results --font /System/Library/Fonts/PingFang.ttc

# Batch process all .txt files in directory with parallel acceleration
python main.py --input input_folder --batch --extensions .txt --parallel

# Generate all data formats but no visualization charts (fast processing)
python main.py --input sample.txt --formats json,csv,excel --no-viz

# Only generate word cloud and word frequency charts with low resolution
python main.py --input sample.txt --viz wordcloud,word_frequency --dpi 72

# Use advanced visualization options
python main.py --input sample.txt --advanced-viz pie,vertical,length
```

## Future Enhancement Suggestions

For further development, I suggest future versions could consider adding the following features and improvements:

### Content Analysis Extensions

- **Topic Modeling**: Integrate LDA (Latent Dirichlet Allocation) topic modeling to automatically discover topic structures in text
- **Text Similarity Comparison**: Add multi-text similarity analysis to compare relationships between different texts
- **Time Series Analysis**: For text collections with timestamps, provide trend analysis of language usage changes over time
- **Associated Word Analysis**: Explore associations and co-occurrence relationships between words for deeper semantic understanding

### User Interface Optimization

- **Web Interface**: Develop browser-based web interface without requiring command line or local installation
- **More Visualization Options**: Provide richer interactive visualization options (such as heatmaps, network diagrams, etc.)
- **Batch Task Queue**: Implement task queue system for better management of large batch processing tasks
- **Real-time Analysis Dashboard**: Provide real-time text analysis dashboard dynamically displaying analysis results

### Technical Improvements

- **GPU Acceleration Support**: Provide GPU acceleration options for large text processing
- **More Text Format Support**: Extend direct parsing capabilities for PDF, Word, web page and other formats
- **Machine Learning Enhancement**: Integrate more advanced machine learning models to improve accuracy of sentiment analysis and keyword extraction

### Integration and Extensibility

- **API Expansion**: Provide complete RESTful API for easy integration with other systems
- **Plugin System**: Develop plugin architecture allowing community members to contribute new features and extensions
- **Database Integration**: Add connectors to common database systems for large-scale text processing

## Acknowledgments

This program was completed with assistance from Claude 3.7 Sonnet and Deepseek. 