# Ch04 进阶认识Python语法
# Task01 面向对象编程
# 题目2 初始化app
# 说明：在MobileApp类中，定义一个方法feature_showcase，该方法输出“这是一个通用的移动应用”。
# 在SocialApp类中，重写feature_showcase方法，使其输出“这是一个社交应用，可以添加好友和发布短视频”。
# 在GameApp类中，重写feature_showcase方法，使其输出“这是一个游戏应用，支持多人游戏和内购项目”。
# 然后，创建一个MobileApp的对象，一个SocialApp的对象和一个GameApp的对象，并放入一个列表中。遍历这个列表，并对每个对象调用feature_showcase方法，观察输出。
# 期望的输出如下：
#     这是一个通用的移动应用
#     这是一个社交应用，可以添加好友和发布短视频
#     这是一个游戏应用，支持多人游戏和内购项目 

class MobileApp:
    # 初始化app
    def __init__(self):
        self.app_name = input("Please enter the app name: ")
        self.download_count = int(input("Please enter the download count: "))
        self.rating = float(input("Please enter the rating score: "))
        
    # 设置一个方法来设置 app 的各个属性
    def set_app_info(self, app_name, download_count, rating):
        self.app_name = app_name
        self.download_count = download_count
        self.rating = rating

    # 设置一个方法来获取 app 的属性值
    def get_app_info(self):
        app_info = f"{self.app_name} {self.download_count} {self.rating}"
        return app_info.title()
    
    # 定义一个方法feature_showcase，该方法输出“这是一个通用的移动应用”。
    def feature_showcase(self):
        print("这是一个通用的移动应用。")

# 创建社交软件类SocialApp，继承自MobileApp类
class SocialApp(MobileApp):
    def __init__(self):
        # 调用父类的构造方法
        super().__init__()
        self.friends_count = int(input("Please enter the number of the friends: "))
        self.supports_short_video = input("Please enter the Yes/No for the short video supporting status: ")
        self.privacy_level = input("Please enter the privacy level: ")
    
    def print_info(self):
        app_info = f"{self.app_name} {self.download_count} {self.rating} {self.friends_count} {self.supports_short_video} {self.privacy_level}"
        print(app_info.title())
    
    # 重写feature_showcase方法，使其输出“这是一个社交应用，可以添加好友和发布短视频”。
    def feature_showcase(self):
        print("这是一个社交应用，可以添加好友和发布短视频。")

# 创建游戏应用类GameApp，继承自MobileApp类，
class GameApp(MobileApp):
    def __init__(self):
        # 调用父类的构造方法
        super().__init__()
        self.game_type = input("Please enter the game type: ")
        self.multiplayer = input("Please enter Yes/No for the game is multiplayer: ")
        self.in_app_purchases_count = input("Pleasr enter Yes/No for there is a purchases count in app: ")
    def print_info(self):
        app_info = f"{self.app_name} {self.download_count} {self.rating} {self.game_type} {self.multiplayer} {self.in_app_purchases_count}"
        print(app_info.title())
    # 重写feature_showcase方法，使其输出“这是一个游戏应用，支持多人游戏和内购项目”。
    def feature_showcase(self):
        print("这是一个游戏应用，支持多人游戏和内购项目。")

# 然后，创建一个MobileApp的对象，一个SocialApp的对象和一个GameApp的对象，并放入一个列表中。遍历这个列表，
# 并对每个对象调用feature_showcase方法，观察输出。
# 期望的输出如下：
#     这是一个通用的移动应用
#     这是一个社交应用，可以添加好友和发布短视频
#     这是一个游戏应用，支持多人游戏和内购项目 
mobileapp_01 = MobileApp()
socialapp_01 = SocialApp()
gameapp_01 = GameApp()

app_list = [mobileapp_01, socialapp_01, gameapp_01]

for app in app_list:
    app.feature_showcase()
