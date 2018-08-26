#-*-coding:utf-8-*-
import jieba
from wordcloud import WordCloud
import matplotlib.pyplot as plt
 
s1 = "未来十年 你的消费可能会发生这5大变化"
 
s2 = "如何看懂财务报表及其背后隐藏着的玄机"
 
s3 = "全球最大资管公司已满仓A股！外资究竟看上了A股什么？"
 
mylist = [s1, s2, s3]
word_list = [" ".join(jieba.cut(sentence)) for sentence in mylist]
new_text = ' '.join(word_list)
wordcloud = WordCloud(font_path="STZHONGS.TTF", background_color="gray").generate(new_text)
plt.imshow(wordcloud)
plt.axis("off")
plt.show()