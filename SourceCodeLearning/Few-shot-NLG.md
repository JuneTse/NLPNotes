## Few-Shot NLG代码学习

### 模型
* 模型输入
> * context: infobox的信息，属性名和对应的值使用bpe编码，得到id形式的矩阵, 输入到GPT模型中[batchsize,len], 用来生成第一个单词。
> * 


### 模型函数
* self.define_decoder_arch(): 对context进行编码，得到输出
* self.lookup_all_embedding(): 对输入的Table和输出的句子中的单词做embedding, 并和单词的位置、field类型信息的embedding拼接在一起
