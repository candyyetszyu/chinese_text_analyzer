# -*- coding: utf-8 -*-
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm
from wordcloud import WordCloud
import seaborn as sns
import os
import numpy as np

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

# 詞性映射（簡體/英文 -> 繁體）
POS_MAPPING = {
    # 詞性標注集
    'n': '名詞',
    'v': '動詞',
    'adj': '形容詞',
    'adv': '副詞',
    'prop': '代詞',
    'prep': '介詞',
    'conj': '連詞',
    'num': '數詞',
    'meas': '量詞',
    'aux': '助詞',
    'punc': '標點',
    'nr': '人名',
    'ns': '地名',
    'nt': '機構名',
    'nz': '專有名詞',
    'a': '形容詞',
    'd': '副詞',
    'm': '數量詞',
    'r': '代詞',
    'c': '連詞',
    'p': '介詞',
    'u': '助詞',
    'xc': '其他',
    'w': '標點',
    'f': '方位詞',
    'g': '語素',
    'h': '前綴',
    'k': '後綴',
    'j': '簡稱',
    'l': '習用語',
    'i': '成語',
    'q': '量詞',
    's': '處所詞',
    't': '時間詞',
    'tg': '時語素',
    'vd': '副動詞',
    'vn': '名動詞',
    'y': '語氣詞',
    'z': '狀態詞',
    'ag': '形語素',
    'dg': '副語素',
    'ng': '名語素',
    'vg': '動語素',
    # 擴展的詞性映射
    'eng': '英文詞',
    'b': '區別詞',
    'zg': '狀態語素',
    'rg': '代詞語素',
    'mg': '數語素',
    'o': '擬聲詞',
    'e': '嘆詞',
    'x': '非語素字',
    'xx': '非語素字',
    'zh': '非語素字詞',
    'vf': '趨向詞',
    'vi': '不及物動詞',
    'vq': '動詞後綴',
    'al': '形容詞性成語',
    'an': '名形詞',
    'ad': '副形詞',
    'bl': '區別詞性成語',
    'dl': '副詞性成語',
    'il': '成語',
    'nl': '名詞性成語',
    'rl': '代詞性成語',
    'tl': '時間詞性語素',
    'vl': '動詞性成語',
    'zl': '狀態詞性成語',
    'rr': '人稱代詞',
    'rz': '指示代詞',
    'rx': '代詞性語素',
    'nrf': '音譯人名',
    'per': '人名',
    'loc': '地名',
    'org': '機構名',
    'time': '時間詞',
    'nrt': '音譯人名',
    'noun': '名詞',
    'verb': '動詞',
    'adj': '形容詞',
    'adv': '副詞',
    'pron': '代詞',
    'prep': '介詞',
    'conj': '連詞',
    'art': '冠詞',
    'num': '數詞',
    'int': '嘆詞',
    'aux': '助詞',
    'punc': '標點',
    'acronym': '縮略語',
    'sub': '代詞',
    'quantifier': '量詞',
    'det': '限定詞',
    'particle': '助詞',
    'exclamation': '嘆詞',
    'modal': '情態詞',
    'functional': '功能詞',
    'idiom': '成語',
    'slang': '俚語',
    'phrase': '短語',
    'proverb': '諺語',
    'interjection': '嘆詞'
}

# 實體類型映射（英文 -> 繁體）
ENTITY_MAPPING = {
    'person': '人物',
    'location': '地點',
    'organization': '組織'
}

# 情感標籤映射（英文 -> 繁體）
SENTIMENT_MAPPING = {
    'positive': '正面情感',
    'negative': '負面情感',
    'neutral': '中性情感'
}

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
        categories = [SENTIMENT_MAPPING['positive'], SENTIMENT_MAPPING['negative'], SENTIMENT_MAPPING['neutral']]
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
    def create_visualization_report(results, output_dir='visualization', prefix='', font_path=None):
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