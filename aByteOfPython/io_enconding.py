# encoding=utf-8
import io

f = io.open("abc.txt", "wt", encoding="utf-8")
f.write(u"瘦肉i推荐哦i就为佛为i就覅就Rios解耦i欸我囧")
f.close()

text = io.open("abc.txt", encoding="utf-8").read()
print(text)