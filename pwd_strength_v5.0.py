"""
    作者:北辰
    功能:判断密码强弱
    版本:5.0
    日期:03/07/2018
    2.0新增功能:循环的终止
    3.0新增功能:保存密码及强度到文件中
    4.0新增功能:读取文件中的密码
    5.0新增功能:定义一个password工具类
"""

class PasswordTool:
    """
        密码工具类
    """
    def __init__(self,password):
        #类的属性
        self.password=password
        self.strength_level=0
    # 类的方法
    def process_password(self):
        """
        处理字符串
        """
        # 规则1:密码长度大于8
        if len(self.password) >= 8:
            self.strength_level += 1
        else:
            print('密码长度至少大于等于8位!')

        # 规则2:密码中含有数字
        if self.check_number_exist():
            self.strength_level += 1
        else:
            print('密码要求包含数字!')

        # 规则3:密码中含有字母
        if self.check_letter_exist():
            self.strength_level += 1
        else:
            print('密码要求包含字母!')

    def check_number_exist(self):
        """
        判断字符串中是否含有数字
        """
        has_number = False

        for c in self.password:
            if c.isnumeric():
                has_number = True
                break

        return has_number

    def check_letter_exist(self):
        """
        判断字符串中是否含有字母
        """
        has_letter = False

        for c in self.password:
            if c.isalpha():
                has_letter = True
                break

        return has_letter

def main():
    """
    主函数
    """
    try_times =  5  #最多尝试次数

    while try_times > 0:
        password=input('请输入一个密码: ')
        # 实例化密码工具对象
        password_tool = PasswordTool(password)

        password_tool.process_password()

        #将密码及对应强度保存到文件中
        f = open('password_v3.0.txt', 'a')  # 打开文件,"添加"模式
        f.write('密码:{},强度:{}\n'.format(password,password_tool.strength_level))
        f.close()    # 关闭文件

        if password_tool.strength_level==3:
            print('恭喜!密码强度合格')
            break
        else:
            print('密码强度不合格!')
            try_times-=1
        print()

    if try_times <=0:
        print('尝试次数过多，密码设置失败!')

if __name__=='__main__':
    main()