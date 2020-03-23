from Crypto.Cipher import AES
import base64
import time


class cryption():
    def __init__(self):
        # key值（密码）
        self.key = 'smyissupercooool'.encode(
            "utf-8")  # 因为在python3中AES传入参数的参数类型存在问题，需要更换为 bytearray , 所以使用encode编码格式将其转为字节格式（linux系统可不用指定编码）
        # vi偏移量
        self.iv = 'smyisnotsocooool'.encode("utf-8")  # 编码
        self.mode = AES.MODE_CBC
        self.BS = AES.block_size
        self.pad = lambda s: s + (self.BS - len(s) % self.BS) * chr(self.BS - len(s) % self.BS)
        self.unpad = lambda s: s[0:-ord(s[-1])]

    # 加密
    def encrypt(self, text):
        text = self.pad(text).encode("utf-8")
        cryptor = AES.new(self.key, self.mode, self.iv)
        # 目前AES-128 足够目前使用(CBC加密)
        ciphertext = cryptor.encrypt(text)
        # base64加密
        return base64.b64encode(bytes(ciphertext))

    # 解密
    def decrypt(self, text):
        # base64解密
        text = base64.b64decode(text)
        cryptor = AES.new(self.key, self.mode, self.iv)
        # CBC解密
        plain_text = cryptor.decrypt(text)
        # 去掉补足的空格用strip() 去掉
        return self.unpad(bytes.decode(plain_text).rstrip('\0'))  # 解密字节？？？

