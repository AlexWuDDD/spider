# 网页基础

## 网页的组成

### HTML骨架

### CSS 皮肤

### JavaScript 肌肉

### 节点树及节点间的关系

在HTML中，所有标签定义的内容都是节点，他们构成了一个HTML DOM树。

#### 什么是DOM？

DOM是W3C（万维网联盟）的标准，Document Object Model,即文档对象模型。
它定义了访问HTML和XML的标准：
>W3C文档对象模型（DOM）是中立于平台和语言的接口，
>它允许程序和脚本动态地访问和更新文档的内容、结构和样式。

W3C DOM标准被分为3个不同的部分。
- 核心DOM 针对任何结构文档的标准模型
- XML DOM 针对XML文档的标准模型
- HTML DOM 针对HTML文档的标准模型

根据W3C的HTML DOM标准，HTML文档中的所有内容都是节点。
通过HTML DOM，所有节点均可通过JavaScript访问，
所有HTML节点元素均可被修改，也可以被创建或删除。

### 选择器

参考网址：https://www.w3school.com.cn/cssref/css_selectors.asp