import re

# 把'小王 2024/3/14 17:34:07'这种格式都改成'2024-3-14 17:34:07 小王'这种格式
def format_messages(file_path):
    # 读取原文件内容
    with open(file_path, 'r', encoding='utf-8') as infile:
        lines = infile.readlines()

    # 格式化后的内容存储在列表中
    formatted_lines = []

    for line in lines:
        # 使用正则表达式匹配目标格式
        match = re.match(r'(.+?)\s+(\d{4})/(\d{1,2})/(\d{1,2})\s+(\d{1,2}:\d{2}:\d{2})', line)
        if match:
            sender = match.group(1)  # 发送者
            year = match.group(2)  # 年
            month = match.group(3)  # 月
            day = match.group(4)  # 日
            time = match.group(5)  # 时间

            # 重新格式化为新格式
            new_format = f"{year}-{month}-{day} {time} {sender}\n"
            formatted_lines.append(new_format)
        else:
            # 如果没有匹配，则原样保留
            formatted_lines.append(line)

    # 将格式化后的内容写回原文件
    with open(file_path, 'w', encoding='utf-8') as outfile:
        outfile.writelines(formatted_lines)


# 调用函数
format_messages('1.txt')
