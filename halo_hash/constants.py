from toolkit.logger import Logger
from toolkit.fileutils import Fileutils
from toolkit.telegram import Telegram

logging = Logger(10)
SECDIR = "../../"
STGY = "strategies/"
FUTL = Fileutils()
CONFIG = FUTL.get_lst_fm_yml(SECDIR + "halo-hash.yml")
CRED = CONFIG["finvasia"]
TGRAM = Telegram(**CONFIG["telegram"])
