

# 写数据
def file_write(path, data):
    with open(path, "w", encoding="utf-8") as f:
        f.writelines(data)

# 读数据
def file_read(path):
    with open(path, "r", encoding="utf-8") as f:
        data = f.read()
    return data


# 获取文件名
def get_file_names(directory):
    file_names = []
    for file_name in os.listdir(directory):
        if os.path.isfile(os.path.join(directory, file_name)):
            file_names.append(file_name)
    return file_names
