# CH04 进阶认识Python语法
# Task01 面向对象编程
# 题目01：移动app
# 说明：定义一个移动应用类MobileApp
# 属性：应用名称app_name、下载量download_count、评分rating；
# 方法：设置应用的各个属性的set_app_info方法；获取各属性值的get_app_info方法。

class MobileApp:
    def __init__(self, app_name, download_count, rating):
        self.app_name = app_name
        self.download_count = download_count
        self.rating = rating
    
    # 设置一个方法，来设置应用的各个属性
    def set_spp_info(self, app_name, download_count, rating):
        self.app_name = app_name
        self.download_count = download_count
        self.rating = rating

    # 设置一个方法来获取 app 的属性值
    def get_app_info(self):
        app_info = f"{self.app_name} {self.download_count} {self.rating}"
        return app_info.title()

# 实例一
app_01 = MobileApp("wechat", 9527, 5.0)
print(app_01.get_app_info())
app_01.set_spp_info("youchat", 17000, 2.0)
print(app_01.get_app_info())

# 实例二
app_02 = MobileApp("edge", 2897, 4.0)
print(app_02.get_app_info())
app_02.set_spp_info("chrome", 847000, 9.0)
print(app_02.get_app_info())