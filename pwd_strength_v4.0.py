"""
    作者:北辰
    功能:判断密码强弱
    版本:4.0
    日期:20/06/2018
    2.0新增功能:循环的终止
    3.0新增功能:保存密码及强度到文件中
    4.0新增功能:读取文件中的密码
"""

def check_number_exist(password_str):
    """
    判断字符串中是否含有数字
    """
    has_number = False

    for c in password_str:
        if c.isnumeric():
            has_number = True
            break

    return has_number

def check_letter_exist(password_str):
    """
    判断字符串中是否含有字母
    """
    has_letter = False

    for c in password_str:
        if c.isalpha():
            has_letter = True
            break

    return has_letter

def main():
    """
    主函数
    """
    # try_times =  5  #最多尝试次数
    #
    # while try_times > 0:
    #     password=input('请输入一个密码: ')
    #
    #     # 密码强度
    #     strength_level = 0
    #
    #     # 规则1:密码长度大于8
    #     if len(password)>=8:
    #         strength_level+=1
    #     else:
    #         print('密码长度至少大于等于8位!')
    #
    #     # 规则2:密码中含有数字
    #     if check_number_exist(password):
    #         strength_level+=1
    #     else:
    #         print('密码要求包含数字!')
    #
    #     # 规则3:密码中含有字母
    #     if check_letter_exist(password):
    #         strength_level+=1
    #     else:
    #         print('密码要求包含字母!')
    #
    #     #将密码及对应强度保存到文件中
    #     f = open('password_v3.0.txt', 'a')  # 打开文件,"添加"模式
    #     f.write('密码:{},强度:{}\n'.format(password,strength_level))
    #     f.close()    # 关闭文件
    #
    #     if strength_level==3:
    #         print('恭喜!密码强度合格')
    #         break
    #     else:
    #         print('密码强度不合格!')
    #         try_times-=1
    #     print()
    #
    # if try_times <=0:
    #     print('尝试次数过多，密码设置失败!')

    # 读取文件
    f=open('password_v3.0.txt','r')

    # 方法1: read() 返回值为包含整个文件内容的字符串
    content = f.read()
    print(content)

    # 方法2: readline() 返回值为包含文件下一行内容的字符串
    line = f.readline()
    print(line)
    line = f.readline()
    print(line)

    # 方法3: readlines() 返回值为整个文件内容的列表,每项是以换行符为结尾的一行字符串
    lines = f.readlines()
    for line in lines:
        print('read: {}'.format(line))

    f.close


if __name__=='__main__':
    main()