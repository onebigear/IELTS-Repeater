# IELTS Repeater 雅思复读机

## **Background**

平时听写完单词错一堆还没人给我听写，只能自己写个程序给自己听写这个亚子。

## **Install and run**

首先安装依赖库

``` bash
pip install -r requirements.txt
```

然后

``` bash
python run.py
```

需要注意的是，在运行之前你需要在项目目录提供一个*words.txt*，可以查看我提供Sample，单词由空格分开。

## **Details**

### GetVoice

GetVoice通过传入一个单词，检查本地是否有缓存记录，没有就调用api下载语音文件。

### GetWord

通过读取*words.txt*得到单词列表，并调用GetVoice下载对应的语音资源

### GenerateList

读取*words.txt*然后使用`random.shuffle()`打乱单词列表取前五十个单词，生成新的单词列表*newWordList.txt*,便于听写完成后订正使用。

### Dictation

读取*newWordList.txt*，在语音库中寻找对应的发音文件，并使用playsound播放。

### run

可以直接运行的文件，本项目的逻辑代码

## **Future Work**

   1. 希望能找到更多的语音库，丰富语音资源。
   2. 希望可以在听写时随机更换口音贴近考试内容。
   3. 在听写列表的选择上也可以加入反馈机制，让错误率更高的词汇有更大的可能出现在下一次的听写列表当中。
   4. 统计每一个单词的错误率，生成可视化报告。

## **Contact Me**

* Wechat：chenfangzhou001
* QQ：    935562189
* Email:  cfz1885@gmail.com
