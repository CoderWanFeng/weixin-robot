# image转base64
import base64, os

path = 'image//'
files = os.listdir(path)
id = 329
for file in files:
    # print(file)
    with open(path + file, "rb") as f:  # 转为二进制格式
        base64_data = base64.b64encode(f.read())  # 使用base64进行加密
        # print(base64_data)
        s = base64_data.decode()
        res = open('1.csv', 'a+')  # 写成文本格式

        id += 1
        res.write(str(id) + ',"data:image/jpeg;base64,' + s+'"')
        res.write('\n')
