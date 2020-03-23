import tkinter
import weChatAccess
import encryption
import time


class SafeChatGui(object):
    def __init__(self):
        self.root = tkinter.Tk()
        # 给主窗口设置标题内容
        self.root.title("safeChat --by Samuel Shi")
        # 创建一个输入框,并设置尺寸
        self.ip_input = tkinter.Entry(self.root, width=50)
        # 创建一个回显列表
        self.display_info = tkinter.Listbox(self.root, width=50)
        # 创建一个查询结果的按钮
        self.result_button = tkinter.Button(self.root, command=self.sendMsg, text="submit")
        #
        self.ip_msg = ''
        #
        self.msg_to_decrypt = ''
        # 创建一个输入框,并设置尺寸
        self.ip_input2 = tkinter.Entry(self.root, width=50)
        # 创建一个回显列表
        self.display_info2 = tkinter.Listbox(self.root, width=50)
        # 创建一个查询结果的按钮
        self.result_button2 = tkinter.Button(self.root, command=self.deCrypt, text="decryption")
        # initialize the key an iv
        self.pc = encryption.cryption()

    # 完成布局
    def gui_arrang(self):
        self.ip_input.pack()
        self.display_info.pack()
        self.result_button.pack()
        self.ip_input2.pack()
        self.display_info2.pack()
        self.result_button2.pack()

    #
    def sendMsg(self):
        self.ip_msg = self.ip_input.get()
        plaintext = self.ip_msg
        e = self.pc.encrypt(plaintext + str(int(time.time() / 10)))  # encryption
        d = self.pc.decrypt(e)  # decryption
        print("encrypted:%s" % e.decode("utf-8"))
        print("decrypted:%s" % d)
        print("length:%s" % len(d))
        self.update(e.decode("utf-8"))
        self.display_info.insert(0, "")
        self.display_info.insert(0, "Message sent safely: "+plaintext)
        self.display_info.insert(0, "Message received safely: (Working in progress)" )

    #
    def deCrypt(self):
        self.msg_to_decrypt = self.ip_input2.get()
        decrypted_msg = self.pc.decrypt(self.msg_to_decrypt)  ########
        self.display_info2.insert(0, decrypted_msg)


    def update(self, msg):
        newWechatAccess = weChatAccess.weChatAccess()
        newWechatAccess.sendMsg(msg)

    def initialize():
        # 初始化对象
        FL = SafeChatGui()
        # 进行布局
        FL.gui_arrang()
        # 主程序执行
        tkinter.mainloop()
        pass


