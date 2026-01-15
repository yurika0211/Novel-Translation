import re

def process_text_for_translation(input_file, output_file):
    try:
        with open(input_file, 'r', encoding='utf-8') as f:
            content = f.read()

        # 1. 基础清理：去除 ---, #, *
        content = re.sub(r'-{3,}.*?-{3,}', '', content)
        content = re.sub(r'^-{3,}\s*$', '', content, flags=re.MULTILINE)
        content = re.sub(r'[\#\*]', '', content)
        # 去掉 第{}页的内容
        content = re.sub(r'第\d+页', '', content)

        # 2. 将内容合并为长字符串并按句号「。」切分
        # 注意：这里保留句号，并确保切分后不会留下无意义的空行
        raw_sentences = re.split(r'(?<=。)', content)
        
        cleaned_sentences = []
        for s in raw_sentences:
            stripped = s.strip()
            if stripped:
                cleaned_sentences.append(stripped)

        # 3. 格式化输出：编号 + 原文 + 翻译占位符
        final_output = []
        for i, sentence in enumerate(cleaned_sentences, 1):
            formatted_block = f"<Sentence>: {sentence}\n\n<Translation>：\n"
            final_output.append(formatted_block)

        # 4. 写入文件
        with open(output_file, 'w', encoding='utf-8') as f:
            f.write('\n'.join(final_output))
            
        print(f"处理完成！翻译模板已生成至: {output_file}")
        
    except Exception as e:
        print(f"处理出错: {e}")

# 执行
process_file_name = './page1-10.txt'  # 你的原始 OCR 文件名
output_file_name = './scripts/page1-10.txt'
process_text_for_translation(process_file_name, output_file_name)