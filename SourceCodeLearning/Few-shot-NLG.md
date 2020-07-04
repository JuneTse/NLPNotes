## Few-Shot NLG代码学习
### 数据

* 处理后
> * field2word.txt: field id对应的bpe单词id, 一个field对应三个bpe单词


### 模型
* 模型输入
> * context: infobox的信息，属性名和对应的值使用bpe编码，得到id形式的矩阵, 输入到GPT模型中[batchsize,len], 用来生成第一个单词。
> * gpt_context: ??
> * decoder_field_input_input: ??
> * decoder_pos_input: ??
> * decoder_rpos_input: ??


### 模型函数
* self.define_decoder_arch(): 对context进行编码，得到输出
* self.lookup_all_embedding(): 对输入的Table和输出的句子中的单词做embedding, 并和单词的位置、field类型信息的embedding拼接在一起
* self.decoder_t(self,inputs, inputs_len,x0, past0, hidden0):
> * inputs: decoder_inputs, decoder的输入，输入到GPT模型中，只有单词的id， 没有positon和field信息。
>> * field和位置的embedding在只是计算attention的时候用
> * x0: 输入的第一个单词
