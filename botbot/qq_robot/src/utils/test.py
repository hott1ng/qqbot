import re
text = '艾特ps设计小权，说你好'
# print(text)

pattern = r'搜索：.+?\n+(.*)'

ans = re.findall(r'艾特(.*)，', text)[0]
print(ans)