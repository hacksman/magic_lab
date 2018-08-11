# Magic Lab
这是我的个人实验室，用来记录code中过程中的进阶代码探索
<br>

### 关于python中的@porperty用法
----

**我的理解:** 它的一个核心作用是能将普通的函数像属性那样提取，比如代码中的样例

```
class AfterPayroll(object):
    def __init__(self, name, year, money):
        self.name = name
        self.raw_year = year
        self.raw_money = money

    @property
    def money(self):
        if self.raw_money / 1000 != 0:
            return self.raw_money / 1000
        else:
            return self.raw_money
```
我在这里用@property装饰器定义了一个money，那么即使我这个类中，没有给money属性，我照样可以用，其实它的作用就是能够将方法变成像属性那样去访问，那我为啥要多此一举呢？其实是这样，如果我们对于外界传来的参数有要求时，这个方法就相当有用了，就很像是我们在Mysql中定义数据类型，比如我们定义名字属性时，规定字符不能超过指定长度。定义学生成绩的属性只能是1~100之间

点开@property函数，我们发现，其实它除了常规的将函数变为属性外，还有一些其他的高级功能，他们分别是**deleter**, **getter**, **setter**, 我只说下我今天探索过的setter函数，它是在给类的属性赋值时使用的，并且它的存在必须要有一个爸爸装饰器在，比如我代码示范中的 **@money.setter**，它是基于money这个属性的，没有 **@porperty**下的这个money方法(即属性)，那这个setter也就不存在

由此，我们就可以做很多方便的事情啦，比如我们有这样一个需求，需要将员工的工资，由原来的**元**单位，改为以**千元**作为单位，并且最丧心病狂的是，前端大佬请了一个月的假，他的祖传代码没人能动。核心需求就一点，不能更改调用者方式的情况下，修改后端提供的数据，以满足前端的要求。于是，这个大杀器就派上大用处了。核心逻辑不再赘述，show u the code in [**decorator/porperty_explore.py**](https://github.com/hacksman/magic_lab/blob/master/decorator/property_explore.py)

**另外补充一点，用setter方法时，在定义类的时候一定要将object带上，不然会报错，具体为啥还不知道，望知道的小伙伴告知下~**
 
<br>
## To to
----

- [X] decorator 中的类中 object 一定要加上的说明
- [X] 改造 decorator/porperty_explore.py 代码，使调试更加方便
- [X] 写 decorator/porperty_explore.py 说明