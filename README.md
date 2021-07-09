# DRFHTutorial

学完django, djangorestframework, django-haystack之后我发现，django-haystack还停留在
编写模版的阶段，也就是说不是前后端分离的，然后我开始思考如何将django-haystack与DRF集成，幸运
的是在我准备实现之前我发现了这个开源项目[drf_haystack](https://drf-haystack.readthedocs.io/en/latest/01_intro.html#examples).
它看起来很好，我决定开始了解和学习，然后在以后的项目中使用上。

但是，实际根据我使用的结果没有出现数据，或者说有些数据已经丢失了。

我增加两个数据到数据库中：

![](https://github.com/cs246810/DRFHTutorial/blob/master/create_data.png)

接着创建索引。

然后，测试api搜索:

![](https://github.com/cs246810/DRFHTutorial/blob/master/api_test.png)

结果有点差强人意，确实出现了结果，但是，这里出现的说text为null的数据，显然我没有找到正确的使用drf_haystack
的方法。