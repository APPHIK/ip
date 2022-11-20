"""global configure arguments"""
from Ingram.utils.base import singleton
from Ingram.utils.net import get_user_agent


@singleton
class Config:

    def __init__(self):
        self.TIMEOUT = 3  # (default) will be reset in the run_ingram.py
        self.USERS = ['admin']  # user names for Brute force cracking of weak passwords
        self.PASSWDS = ['abcd1234', 'Abcd1234', 'Admin123', 'admin123', 'hd543211', 'Admin12345', 'admin12345', 'sys12345', 'sys123456', 'sys1234567', 'sys012345', 'sys0123456', 'sys01234567', 'a1234567', 'A1234567', 'a123456', 'A123456', 'a12345', 'A12345', 'a12345678', 'A12345678','a123456789', 'A123456789', 'a1234567890', 'A1234567890', 'a01234567', 'a0123456', 'a012345678', 'a0123456789', 'hd4543211', 'Hd4543211', 'HD543211', 'HD4543211', '12345', '123456', 'Hd543211', 'admin123456', 'Admin123456', 'abc123abc', 'Abcd12345', 'abcd12345', 'asdf1234', 'abc12345', '12345admin', '12345abc', 'abc123abc', '123abc123']
        self.USERAGENT = get_user_agent()  # to save time, we only get user agent once.
        self.PORT = [80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 180, 181, 182, 183, 184, 185, 186, 187, 188, 189, 190, 280, 282, 281, 380, 480, 580, 680, 780, 880, 980, 8000, 8001, 8002, 8003, 8004, 8005, 8006, 8007, 8008, 8009, 8010, 8011, 8012, 8013, 8014, 8015, 8016, 8017, 8018, 8019, 8020, 8383, 8338, 8111, 8777, 8998, 8888, 8080, 8081, 8085, 8086, 8088, 8090, 8181, 2051, 9000, 37777, 49152, 55555]

        # device names
        self.NON_MATCH_DEV = 'other'
        self.HIKVISION = 'hikvision'
        self.DAHUA = 'dahua'
        self.UNIVIEW_NVR = 'uniview-nvr'
        self.DLINK_DCS = 'dlink-dcs'
        self.CCTV = 'cctv'
        self.DVR = 'dvr'  # cve-2018-9995
        self.TENDA_W15E = 'tenda-w15e'
        self.TPLINK = 'tplink'
        self.HUAWEI = 'huawei'


global config
config = Config()
