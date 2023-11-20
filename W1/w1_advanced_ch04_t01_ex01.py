# Ch04 进阶认识Python语法
# Task01 面向对象编程
# 题目1 移动app
# 说明
# 创建社交软件类SocialApp，继承自MobileApp类
# SocialApp类添加额外三个属性：好友数量friends_count、是否支持短视频supports_short_video、隐私等级privacy_level；
# 方法：打印社交软件的所有信息print_info方法。
# 创建游戏应用类GameApp，继承自MobileApp类，
# 添加额外三个属性：游戏类型game_type、是否支持多人multiplayer、内购项目数in_app_purchases_count；
# 方法：打印游戏应用的所有信息print_info方法。
# 定义上述两个类的对象，并分别调用print_info方法，实现各自对象属性信息的输出。

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

# 创建社交软件类SocialApp，继承自MobileApp类
class SocialApp(MobileApp):
    def __init__(self, app_name, download_count, rating, friends_count, supports_short_video, privacy_level):
        super().__init__(app_name, download_count, rating)
        self.friends_count = friends_count
        self.supports_short_video = supports_short_video
        self.privacy_level = privacy_level
    
    def print_info(self):
        app_info = f"{self.app_name} {self.download_count} {self.rating} {self.friends_count} {self.supports_short_video} {self.privacy_level}"
        print(app_info.title())


# 创建游戏应用类GameApp，继承自MobileApp类，
class GameApp(MobileApp):
    def __init__(self, app_name, download_count, rating, game_type, multiplayer, in_app_purchases_count):
        super().__init__(app_name, download_count, rating, )
        self.game_type = game_type
        self.multiplayer = multiplayer
        self.in_app_purchases_count = in_app_purchases_count
    def print_info(self):
        app_info = f"{self.app_name} {self.download_count} {self.rating} {self.game_type} {self.multiplayer} {self.in_app_purchases_count}"
        print(app_info.title())


# 定义社交软件类SocialApp的对象，调用print_info方法，实现对象属性信息的输出。
socialapp_example01 = SocialApp("Wechat", "10100", "4.0", "100", "support_short_video", "level_1")
socialapp_example01.print_info()


# 定义游戏应用类GameApp的对象，调用print_info方法，实现对象属性信息的输出。
gameapp_example01 = GameApp("FM2024", "19000", "9.1", "strategy game", "single-player game", "0")
gameapp_example01.print_info()
