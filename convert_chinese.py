#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Utility script to convert simplified Chinese to traditional Chinese in files
"""

import os
import sys
import argparse

def convert_file(file_path, backup=True):
    """Convert a file from simplified to traditional Chinese"""
    try:
        import opencc
    except ImportError:
        print("請先安裝 OpenCC: pip install opencc-python-reimplemented")
        return False
    
    try:
        # Create backup if requested
        if backup:
            backup_path = file_path + ".bak"
            with open(file_path, 'r', encoding='utf-8') as src:
                with open(backup_path, 'w', encoding='utf-8') as dst:
                    dst.write(src.read())
            print(f"已創建備份文件: {backup_path}")
        
        # Convert content
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Convert to traditional Chinese
        converter = opencc.OpenCC('s2t')
        traditional_content = converter.convert(content)
        
        # Write back to the file
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(traditional_content)
        
        print(f"已將 {file_path} 轉換為繁體中文")
        return True
    
    except Exception as e:
        print(f"轉換 {file_path} 時出錯: {str(e)}")
        return False

def convert_directory(dir_path, extensions=None, recursive=False, backup=True):
    """Convert all files in a directory"""
    if extensions is None:
        extensions = ['.py', '.txt', '.md', '.json']
    
    converted = 0
    failed = 0
    
    # Get all files in directory
    files = []
    if recursive:
        for root, _, filenames in os.walk(dir_path):
            for filename in filenames:
                files.append(os.path.join(root, filename))
    else:
        files = [os.path.join(dir_path, f) for f in os.listdir(dir_path) if os.path.isfile(os.path.join(dir_path, f))]
    
    # Filter by extension
    files = [f for f in files if os.path.splitext(f)[1].lower() in extensions]
    
    # Convert each file
    for file_path in files:
        if convert_file(file_path, backup):
            converted += 1
        else:
            failed += 1
    
    print(f"\n轉換完成: {converted} 個文件已轉換，{failed} 個文件轉換失敗")
    return converted, failed

def main():
    parser = argparse.ArgumentParser(description="將簡體中文轉換為繁體中文")
    parser.add_argument('--file', '-f', help="要轉換的文件路徑")
    parser.add_argument('--dir', '-d', help="要轉換的目錄路徑")
    parser.add_argument('--ext', '-e', help="要轉換的文件擴展名，用逗號分隔 (例如: .py,.txt)")
    parser.add_argument('--recursive', '-r', action='store_true', help="遞歸處理子目錄")
    parser.add_argument('--no-backup', action='store_true', help="不創建備份文件")
    
    args = parser.parse_args()
    
    # Parse extensions if provided
    extensions = None
    if args.ext:
        extensions = []
        for ext in args.ext.split(','):
            ext = ext.strip()
            if not ext.startswith('.'):
                ext = '.' + ext
            extensions.append(ext)
    
    # Convert file or directory
    if args.file:
        convert_file(args.file, not args.no_backup)
    elif args.dir:
        convert_directory(args.dir, extensions, args.recursive, not args.no_backup)
    else:
        # If no arguments provided, show help
        parser.print_help()
        print("\n範例使用方法:")
        print("  轉換單個文件:   python convert_chinese.py --file visualization.py")
        print("  轉換整個目錄:   python convert_chinese.py --dir . --ext .py")
        print("  轉換整個專案:   python convert_chinese.py --dir . --recursive")

if __name__ == "__main__":
    main()