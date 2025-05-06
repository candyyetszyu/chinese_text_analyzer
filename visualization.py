# -*- coding: utf-8 -*-
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm
from wordcloud import WordCloud
import seaborn as sns
import os
import numpy as np
import json

# Configure matplotlib to use Chinese font
CHINESE_FONT_PATH = '/System/Library/Fonts/STHeiti Light.ttc'
if os.path.exists(CHINESE_FONT_PATH):
    plt.rcParams['font.family'] = fm.FontProperties(fname=CHINESE_FONT_PATH).get_name()
    plt.rcParams['axes.unicode_minus'] = False  # Correctly display minus sign
    DEFAULT_CHINESE_FONT = CHINESE_FONT_PATH
else:
    # Fallback to other Chinese fonts on macOS
    mac_font_paths = [
        "/System/Library/Fonts/PingFang.ttc",
        "/System/Library/Fonts/Hiragino Sans GB.ttc",
        "/System/Library/Fonts/Songti.ttc",
        "/Library/Fonts/Arial Unicode.ttf"
    ]
    
    DEFAULT_CHINESE_FONT = None
    for font_path in mac_font_paths:
        if os.path.exists(font_path):
            plt.rcParams['font.family'] = fm.FontProperties(fname=font_path).get_name()
            plt.rcParams['axes.unicode_minus'] = False
            DEFAULT_CHINESE_FONT = font_path
            break
    
    if DEFAULT_CHINESE_FONT is None:
        pass

# 定義資源文件的基礎路徑
RESOURCES_PATH = os.path.join(
    os.path.dirname(os.path.abspath(__file__)),
    'resources'
)

# 從資源文件加載映射
def load_mapping_from_json(filename):
    # 首先嘗試從 mappings 子目錄加載
    filepath = os.path.join(RESOURCES_PATH, 'mappings', filename)
    if os.path.exists(filepath):
        try:
            with open(filepath, 'r', encoding='utf-8') as f:
                return json.load(f)
        except Exception as e:
            print(f"無法從 mappings 目錄加載映射文件 {filename}: {e}")
            # 如果從 mappings 目錄加載失敗，嘗試從根目錄加載（向後兼容）
            root_filepath = os.path.join(RESOURCES_PATH, filename)
            if os.path.exists(root_filepath):
                try:
                    with open(root_filepath, 'r', encoding='utf-8') as f:
                        return json.load(f)
                except Exception as e:
                    print(f"無法加載映射文件 {filename}: {e}")
                    return {}
            return {}
    else:
        # 如果 mappings 目錄中沒有找到，嘗試從根目錄加載（向後兼容）
        root_filepath = os.path.join(RESOURCES_PATH, filename)
        if os.path.exists(root_filepath):
            try:
                with open(root_filepath, 'r', encoding='utf-8') as f:
                    return json.load(f)
            except Exception as e:
                print(f"無法加載映射文件 {filename}: {e}")
                return {}
        else:
            print(f"映射文件不存在: {filepath} 或 {root_filepath}")
            return {}

# 載入詞性、實體和情感標籤映射
POS_MAPPING = load_mapping_from_json('pos_mapping.json')
ENTITY_MAPPING = load_mapping_from_json('entity_mapping.json')
SENTIMENT_MAPPING = load_mapping_from_json('sentiment_mapping.json')

class Visualizer:
    @staticmethod
    def plot_word_frequency(word_freq, top_n=20, title='詞頻統計', save_path=None, figsize=(12, 6)):
        """繪製詞頻條形圖"""
        top_words = dict(sorted(word_freq.items(), key=lambda x: x[1], reverse=True)[:top_n])
        
        plt.figure(figsize=figsize)
        # 使用更高效的繪圖設置
        with plt.style.context('fast'):
            ax = sns.barplot(x=list(top_words.values()), y=list(top_words.keys()))
        
        # 在每個條形上顯示數值
        for i, v in enumerate(list(top_words.values())):
            ax.text(v + 0.1, i, str(v), va='center')
            
        plt.title(title)
        plt.xlabel('頻率')
        plt.ylabel('詞語')
        plt.tight_layout()
        
        if save_path:
            plt.savefig(save_path, dpi=300, bbox_inches='tight')
        
        plt.close()
    
    @staticmethod
    def generate_wordcloud(word_freq, title='詞雲圖', save_path=None, figsize=(10, 8), 
                          font_path=None, background_color='white', max_words=200):
        """生成詞雲"""
        # 使用全局中文字體設置，除非指定了其他字體
        if font_path is None:
            # 首先嘗試使用我們已確認的全局中文字體
            if 'DEFAULT_CHINESE_FONT' in globals() and DEFAULT_CHINESE_FONT:
                font_path = DEFAULT_CHINESE_FONT
            else:
                # 嘗試其他常見的中文字體路徑
                possible_fonts = [
                    '/System/Library/Fonts/STHeiti Light.ttc',
                    '/System/Library/Fonts/PingFang.ttc',
                    '/System/Library/Fonts/Hiragino Sans GB.ttc',
                    '/System/Library/Fonts/Songti.ttc',
                    '/Library/Fonts/Arial Unicode.ttf',
                    None
                ]
                
                for font in possible_fonts:
                    if font is None or os.path.exists(font):
                        font_path = font
                        break
        else:
            if not os.path.exists(font_path):
                if 'DEFAULT_CHINESE_FONT' in globals() and DEFAULT_CHINESE_FONT:
                    font_path = DEFAULT_CHINESE_FONT
                else:
                    font_path = None
        
        # 生成詞雲的核心代碼
        try:
            # 設置詞雲參數
            wc_kwargs = {
                'background_color': background_color,
                'width': 800,
                'height': 600,
                'max_words': max_words,
                'collocations': False,
                'mode': 'RGBA'  # 使用RGBA模式，支持透明背景
            }
            
            # 如果確實有字體存在，則使用它
            if font_path and os.path.exists(font_path):
                wc_kwargs['font_path'] = font_path
                
            wc = WordCloud(**wc_kwargs).generate_from_frequencies(word_freq)
            
            plt.figure(figsize=figsize)
            plt.imshow(wc, interpolation='bilinear')
            plt.axis('off')
            plt.title(title)
            
            if save_path:
                os.makedirs(os.path.dirname(os.path.abspath(save_path)), exist_ok=True)
                plt.savefig(save_path, dpi=300, bbox_inches='tight')
                
            plt.close()
            return True
            
        except Exception as e:
            try:
                # 備用方法：創建一個非常簡單的詞雲，不使用任何字體
                wc = WordCloud(background_color=background_color, width=800, height=600, 
                               max_words=max_words, collocations=False).generate_from_frequencies(word_freq)
                
                plt.figure(figsize=figsize)
                plt.imshow(wc, interpolation='bilinear')
                plt.axis('off')
                plt.title("詞雲圖 (簡化版)")
                
                if save_path:
                    plt.savefig(save_path, dpi=300, bbox_inches='tight')
                
                plt.close()
                return True
                
            except Exception as e2:
                return False
    
    @staticmethod
    def plot_pos_distribution(pos_freq, title='詞性分布', save_path=None, figsize=(10, 6)):
        """繪製詞性分布圖"""
        # 將詞性標籤轉換為繁體中文
        pos_freq_translated = {}
        for pos, freq in pos_freq.items():
            translated_pos = POS_MAPPING.get(pos, pos)  # 如果找不到映射，保留原始標籤
            pos_freq_translated[translated_pos] = freq
        
        plt.figure(figsize=figsize)
        with plt.style.context('fast'):
            ax = sns.barplot(x=list(pos_freq_translated.values()), y=list(pos_freq_translated.keys()))
        
        # 在每個條形上顯示數值
        for i, v in enumerate(list(pos_freq_translated.values())):
            ax.text(v + 0.1, i, str(v), va='center')
            
        plt.title(title)
        plt.xlabel('頻率')
        plt.ylabel('詞性')
        plt.tight_layout()
        
        if save_path:
            plt.savefig(save_path, dpi=300, bbox_inches='tight')
            
        plt.close()
    
    @staticmethod
    def plot_sentiment_analysis(sentiment_data, title='情感分析', save_path=None, figsize=(8, 5)):
        """繪製情感分析結果圖表"""
        # 從情感分析結果中提取數據
        positive = sentiment_data.get('positive_count', 0)
        negative = sentiment_data.get('negative_count', 0)
        
        # 新增中性情感的顯示
        neutral = 0
        if sentiment_data.get('sentiment_label') == 'neutral':
            neutral = 1
        
        # 繪製條形圖 - 移除情感得分
        plt.figure(figsize=figsize)
        categories = [SENTIMENT_MAPPING.get('positive', '正面情感'), 
                     SENTIMENT_MAPPING.get('negative', '負面情感'), 
                     SENTIMENT_MAPPING.get('neutral', '中性情感')]
        values = [positive, negative, neutral]
        colors = ['green', 'red', 'blue']
        
        with plt.style.context('fast'):
            bars = plt.bar(categories, values, color=colors)
        
        # 添加數值標籤
        for bar in bars:
            height = bar.get_height()
            plt.text(bar.get_x() + bar.get_width()/2., height + 0.1,
                    f'{height}', ha='center', va='bottom')
        
        plt.title(title)
        plt.tight_layout()
        
        if save_path:
            plt.savefig(save_path, dpi=300, bbox_inches='tight')
            
        plt.close()
    
    @staticmethod
    def plot_ngrams(ngrams, top_n=15, title='常見詞組', save_path=None, figsize=(12, 6)):
        """繪製n-gram頻率圖"""
        top_ngrams = dict(sorted(ngrams.items(), key=lambda x: x[1], reverse=True)[:top_n])
        
        plt.figure(figsize=figsize)
        with plt.style.context('fast'):
            ax = sns.barplot(x=list(top_ngrams.values()), y=list(top_ngrams.keys()))
        
        # 在每個條形上顯示數值
        for i, v in enumerate(list(top_ngrams.values())):
            ax.text(v + 0.1, i, str(v), va='center')
            
        plt.title(title)
        plt.xlabel('頻率')
        plt.ylabel('詞組')
        plt.tight_layout()
        
        if save_path:
            plt.savefig(save_path, dpi=300, bbox_inches='tight')
            
        plt.close()
    
    @staticmethod
    def plot_entities(entities, title='命名實體統計', save_path=None, figsize=(12, 8)):
        """繪製命名實體統計圖"""
        # 轉換實體類型名稱為繁體中文
        entity_counts = {}
        for entity_type, entity_list in entities.items():
            if entity_list:  # 只處理非空列表
                # 將英文實體類型轉換為繁體中文
                translated_type = ENTITY_MAPPING.get(entity_type, entity_type)
                entity_counts[translated_type] = len(entity_list)
        
        if not entity_counts:
            return
        
        # 繪製餅圖
        plt.figure(figsize=figsize)
        with plt.style.context('fast'):
            plt.pie(entity_counts.values(), labels=entity_counts.keys(), autopct='%1.1f%%')
        
        plt.title(title)
        plt.axis('equal')  # 使餅圖為正圓形
        
        if save_path:
            plt.savefig(save_path, dpi=300, bbox_inches='tight')
            
        plt.close()
    
    @staticmethod
    def plot_keyword_weights(keywords, top_n=15, title='關鍵詞權重', save_path=None, figsize=(12, 6)):
        """繪製關鍵詞權重圖"""
        top_keywords = dict(sorted(keywords.items(), key=lambda x: x[1], reverse=True)[:top_n])
        
        plt.figure(figsize=figsize)
        with plt.style.context('fast'):
            ax = sns.barplot(x=list(top_keywords.values()), y=list(top_keywords.keys()))
        
        # 在每個條形上顯示數值
        for i, v in enumerate(list(top_keywords.values())):
            ax.text(v + 0.01, i, f'{v:.3f}', va='center')
            
        plt.title(title)
        plt.xlabel('權重')
        plt.ylabel('關鍵詞')
        plt.tight_layout()
        
        if save_path:
            plt.savefig(save_path, dpi=300, bbox_inches='tight')
            
        plt.close()
    
    @staticmethod
    def create_visualization_report(results, output_dir='visualization', prefix='', font_path=None, dpi=300):
        """創建完整的可視化報告
        
        將所有分析結果圖表保存到指定目錄
        """
        # 創建輸出目錄
        os.makedirs(output_dir, exist_ok=True)
        
        # 為避免文件名衝突，添加前綴（例如，文件名）
        if prefix and not prefix.endswith('_'):
            prefix = prefix + '_'
        
        # 詞頻分析
        if 'word_frequency' in results:
            word_freq_path = os.path.join(output_dir, f"{prefix}word_frequency.png")
            Visualizer.plot_word_frequency(
                results['word_frequency'], 
                title='詞頻統計', 
                save_path=word_freq_path
            )
        
        # 詞雲
        if 'word_frequency' in results:
            wordcloud_path = os.path.join(output_dir, f"{prefix}wordcloud.png")
            Visualizer.generate_wordcloud(
                results['word_frequency'], 
                title='詞雲圖', 
                save_path=wordcloud_path,
                font_path=font_path
            )
        
        # 詞性分布
        if 'pos_frequency' in results:
            pos_path = os.path.join(output_dir, f"{prefix}pos_distribution.png")
            Visualizer.plot_pos_distribution(
                results['pos_frequency'], 
                title='詞性分布', 
                save_path=pos_path
            )
        
        # 情感分析
        if 'sentiment' in results:
            sentiment_path = os.path.join(output_dir, f"{prefix}sentiment.png")
            Visualizer.plot_sentiment_analysis(
                results['sentiment'], 
                title='情感分析結果', 
                save_path=sentiment_path
            )
        
        # N-gram分析
        if 'ngrams' in results:
            ngrams_path = os.path.join(output_dir, f"{prefix}ngrams.png")
            Visualizer.plot_ngrams(
                results['ngrams'], 
                title='常見詞組', 
                save_path=ngrams_path
            )
        
        # 命名實體分析
        if 'entities' in results:
            entities_path = os.path.join(output_dir, f"{prefix}entities.png")
            Visualizer.plot_entities(
                results['entities'], 
                title='命名實體統計', 
                save_path=entities_path
            )
        
        # 關鍵詞分析
        if 'keywords' in results:
            keywords_path = os.path.join(output_dir, f"{prefix}keywords.png")
            Visualizer.plot_keyword_weights(
                results['keywords'], 
                title='關鍵詞權重', 
                save_path=keywords_path
            )
        
        return output_dir
    
    @staticmethod
    def plot_advanced_word_frequency(word_freq, top_n=20, categories=None, exclude_words=None, 
                                   title='詞頻統計分析', save_path=None, figsize=(14, 8), 
                                   sort_by='frequency', plot_type='horizontal', color_map='viridis', dpi=300):
        """
        繪製高級詞頻可視化，支持更多自定義選項
        
        Parameters:
        -----------
        word_freq : dict
            詞語頻率字典，格式為 {word: frequency}
        top_n : int
            顯示頻率最高的前N個詞
        categories : dict
            詞語分類字典，格式為 {category_name: [word1, word2, ...]}
        exclude_words : list
            需要排除的詞語列表
        title : str
            圖表標題
        save_path : str
            保存路徑，若為None則不保存
        figsize : tuple
            圖表尺寸
        sort_by : str
            排序方式，可選 'frequency'(頻率), 'alphabetical'(字母順序), 'length'(詞長)
        plot_type : str
            圖表類型，可選 'horizontal'(水平條形圖), 'vertical'(垂直條形圖), 'pie'(餅圖)
        color_map : str
            顏色映射，例如 'viridis', 'plasma', 'inferno', 'magma', 'cividis'
        dpi : int
            圖像解析度，默認為300
        
        Returns:
        --------
        bool
            是否成功生成圖表
        """
        # 過濾排除詞
        if exclude_words:
            word_freq = {word: freq for word, freq in word_freq.items() if word not in exclude_words}
        
        # 按指定方式排序
        if sort_by == 'frequency':
            sorted_words = sorted(word_freq.items(), key=lambda x: x[1], reverse=True)
        elif sort_by == 'alphabetical':
            sorted_words = sorted(word_freq.items(), key=lambda x: x[0])
        elif sort_by == 'length':
            sorted_words = sorted(word_freq.items(), key=lambda x: len(x[0]), reverse=True)
        else:
            sorted_words = sorted(word_freq.items(), key=lambda x: x[1], reverse=True)
            
        # 取前N個詞
        top_words = dict(sorted_words[:top_n])
        
        # 設置顏色
        cmap = plt.get_cmap(color_map)
        
        plt.figure(figsize=figsize)
        
        # 基於分類繪圖
        if categories and plot_type != 'pie':
            # 初始化分類數據
            category_data = {}
            uncategorized_words = []
            
            # 將詞語按分類組織
            for word, freq in top_words.items():
                categorized = False
                for category_name, word_list in categories.items():
                    if word in word_list:
                        if category_name not in category_data:
                            category_data[category_name] = []
                        category_data[category_name].append((word, freq))
                        categorized = True
                        break
                
                if not categorized:
                    uncategorized_words.append((word, freq))
            
            # 添加未分類詞語
            if uncategorized_words:
                category_data['其他'] = uncategorized_words
            
            # 為每個分類創建子圖
            fig, axes = plt.subplots(len(category_data), 1, figsize=figsize)
            fig.suptitle(title, fontsize=16)
            
            for idx, (category_name, word_data) in enumerate(category_data.items()):
                ax = axes[idx] if len(category_data) > 1 else axes
                
                words = [w[0] for w in word_data]
                freqs = [w[1] for w in word_data]
                
                if plot_type == 'horizontal':
                    bars = ax.barh(words, freqs, color=cmap(idx/len(category_data)))
                else:  # vertical
                    bars = ax.bar(words, freqs, color=cmap(idx/len(category_data)))
                    plt.setp(ax.get_xticklabels(), rotation=45, ha='right')
                
                # 添加數值標籤
                for bar in bars:
                    if plot_type == 'horizontal':
                        ax.text(bar.get_width() + 0.1, bar.get_y() + bar.get_height()/2, 
                                f'{bar.get_width()}', va='center')
                    else:
                        ax.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 0.1, 
                                f'{bar.get_height()}', ha='center')
                
                ax.set_title(f"{category_name} ({len(word_data)}詞)")
                
                if plot_type == 'horizontal':
                    ax.set_xlabel('頻率')
                else:
                    ax.set_ylabel('頻率')
            
            plt.tight_layout(rect=[0, 0, 1, 0.95])  # 修正標題和圖表的間距
            
        else:  # 不分類或餅圖
            if plot_type == 'pie':
                # 繪製餅圖
                plt.pie(list(top_words.values()), labels=list(top_words.keys()),
                       autopct='%1.1f%%', colors=[cmap(i/len(top_words)) for i in range(len(top_words))])
                plt.axis('equal')  # 確保餅圖為圓形
                plt.title(title)
            
            elif plot_type == 'horizontal':
                # 繪製水平條形圖
                with plt.style.context('fast'):
                    ax = sns.barplot(x=list(top_words.values()), y=list(top_words.keys()), 
                                    palette=color_map)
                
                # 添加數值標籤
                for i, v in enumerate(list(top_words.values())):
                    ax.text(v + 0.1, i, str(v), va='center')
                
                plt.title(title)
                plt.xlabel('頻率')
                plt.ylabel('詞語')
                
            else:  # vertical
                # 繪製垂直條形圖
                with plt.style.context('fast'):
                    ax = sns.barplot(x=list(top_words.keys()), y=list(top_words.values()),
                                    palette=color_map)
                
                # 添加數值標籤
                for i, v in enumerate(list(top_words.values())):
                    ax.text(i, v + 0.1, str(v), ha='center')
                
                plt.title(title)
                plt.ylabel('頻率')
                plt.xlabel('詞語')
                plt.xticks(rotation=45, ha='right')
            
            plt.tight_layout()
        
        # 保存圖表
        if save_path:
            os.makedirs(os.path.dirname(os.path.abspath(save_path)), exist_ok=True)
            plt.savefig(save_path, dpi=dpi, bbox_inches='tight')
            
        plt.close()
        return True
    
    @staticmethod
    def compare_word_frequencies(freq_data_dict, top_n=15, title='詞頻比較', save_path=None, figsize=(14, 8)):
        """
        比較多個文本或時期的詞頻
        
        Parameters:
        -----------
        freq_data_dict : dict
            包含多個詞頻數據的字典，格式為 {data_name: {word: frequency, ...}, ...}
        top_n : int
            顯示的詞語數量
        title : str
            圖表標題
        save_path : str
            保存路徑
        figsize : tuple
            圖表尺寸
            
        Returns:
        --------
        bool
            是否成功生成圖表
        """
        # 合併所有詞語
        all_words = set()
        for data in freq_data_dict.values():
            all_words.update(data.keys())
        
        # 找出在所有數據中出現頻率最高的詞
        word_total_freq = {}
        for word in all_words:
            word_total_freq[word] = sum(data.get(word, 0) for data in freq_data_dict.values())
        
        # 選取頻率最高的詞
        top_words = dict(sorted(word_total_freq.items(), key=lambda x: x[1], reverse=True)[:top_n])
        
        # 準備繪圖數據
        data_names = list(freq_data_dict.keys())
        words = list(top_words.keys())
        
        # 創建數據矩陣
        data_matrix = []
        for word in words:
            row = [data.get(word, 0) for data in freq_data_dict.values()]
            data_matrix.append(row)
        
        # 創建DataFrame
        import pandas as pd
        df = pd.DataFrame(data_matrix, index=words, columns=data_names)
        
        # 繪製熱圖
        plt.figure(figsize=figsize)
        ax = sns.heatmap(df, annot=True, fmt='d', cmap='YlGnBu')
        
        plt.title(title)
        plt.tight_layout()
        
        # 保存圖表
        if save_path:
            os.makedirs(os.path.dirname(os.path.abspath(save_path)), exist_ok=True)
            plt.savefig(save_path, dpi=300, bbox_inches='tight')
            
        plt.close()
        return True
    
    @staticmethod
    def plot_word_frequency_trends(time_series_data, words, title='詞頻趨勢', save_path=None, figsize=(14, 6)):
        """
        繪製詞頻隨時間變化的趨勢圖
        
        Parameters:
        -----------
        time_series_data : dict
            時間序列詞頻數據，格式為 {time_point: {word: frequency, ...}, ...}
        words : list
            要顯示趨勢的詞語列表
        title : str
            圖表標題
        save_path : str
            保存路徑
        figsize : tuple
            圖表尺寸
            
        Returns:
        --------
        bool
            是否成功生成圖表
        """
        # 整理數據
        time_points = sorted(time_series_data.keys())
        
        plt.figure(figsize=figsize)
        
        # 為每個詞繪製一條線
        for word in words:
            freq_over_time = [time_series_data[t].get(word, 0) for t in time_points]
            plt.plot(time_points, freq_over_time, marker='o', linewidth=2, label=word)
        
        plt.title(title)
        plt.xlabel('時間點')
        plt.ylabel('詞頻')
        plt.legend()
        plt.grid(True, linestyle='--', alpha=0.7)
        
        # 保存圖表
        if save_path:
            os.makedirs(os.path.dirname(os.path.abspath(save_path)), exist_ok=True)
            plt.savefig(save_path, dpi=300, bbox_inches='tight')
            
        plt.close()
        return True