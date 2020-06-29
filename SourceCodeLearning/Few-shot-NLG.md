## Few-Shot NLG代码学习

### 模型
* 模型输入
> * context: infobox的信息，属性名和对应的值使用bpe编码，得到id形式的矩阵, 输入到GPT模型中[batchsize,len], 用来生成第一个单词。
> * 
