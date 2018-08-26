

## Rouge: Recall-Oriented Understudy for Gisting Evaluation

* 简介

  > * 是自动文摘和机器翻译的评测指标
  > * 通过比较自动生成的摘要summary和参考摘要reference，计算得到相应的分值
  > * 用来衡量自动生成的摘要或翻译与参考摘要之间的“相似度”

* Rouge-L：

  > * L表示最长公共子序列
  > * 一篇文档通常有多个参考摘要，这是取单个Rouge-L值最大的作为单个数据的测试结果
  > * 计算方式如下：

$$
Recall_{lcs}= \frac{LCS(X, Y)}{len(Y)}\\

Precision_{lcs} = \frac{LCS(X, Y)}{len(X)}\\

Rouge-l=\frac{(1+\beta^2)Recall_{lcs}*Precision_{lcs}}{Recall_{lcs}+\beta^2*Precision_{lcs}}\\

\beta = \frac{Precision_{lcs}}{Recall_{lcs}+e^{-12} }\\
$$

