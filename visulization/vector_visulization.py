#coding:utf-8
from sklearn.manifold import TSNE
import matplotlib.pyplot as plt
import numpy as np
#可视化词向量
def plot_with_labels(low_dim_embs,labels,filename='tsne.png'):
    assert low_dim_embs.shape[0]>=len(labels), "More labels than embeddings"
    plt.figure(figsize=(18,18))
    for i,label in enumerate(labels):
        x,y=low_dim_embs[i,:]
        plt.scatter(x,y)
        plt.annotate(label,
                     xy=(x,y),
                     xytext=(5,2),
                     textcoords='offset points',
                     ha='right',
                     va='bottom')
        plt.savefig(filename)
        

def visulize_vectors(embeddings,labels,plot_only=500):
    '''
    embeddings: 单词或句子向量
    labels: 或句子列表
    '''
    #降维可视化
    tsne=TSNE(perplexity=30,n_components=2,init='pca',n_iter=5000)
    #降维
    low_dim_embs=tsne.fit_transform(embeddings[:plot_only,:])
    plot_with_labels(low_dim_embs,labels)
    
if __name__=="__main__":
    embeddings=np.random.rand(50,128)
    labels=list(range(50))
    visulize_vectors(embeddings,labels)
    
