class Board:
    callback = None

    def __init__(self, params):
        # 初期化処理の実装
        # # PCI/PCIeデバイスの場合はここでオープン
        # # USBデバイスの場合もここでオープン
        # # 1000Hz サンプリングでボードを開く
        # # 変換処理はまだ開始しない
        raise Exception('this method is not implemented')

    def __del__(self):
        # 終了処理の実装
        # # 参照されなくなった時点で呼ばれる
        # # PCI/PCIeデバイスの場合はここでクローズ
        # # USBデバイスの場合もここでクローズ
        raise Exception('this method is not implemented')

    def board_name(self):
        # "AIO000"や"USB-DAC1616"など文字列を返す
        pass

    def board_type(self):
        # "USB"や"PCI"など文字列を返す
        pass

    def start_ad_sampling(self):
        raise Exception('this method is not implemented')

    def start_ad_sampling_callback_mode(self, callback):
        self.callback = callback
        raise Exception('this method is not implemented')

    def stop_ad_sampling(self):
        raise Exception('this method is not implemented')

    def get_ad_sampling_freq(self):
        raise Exception('this method is not implemented')

    def set_ad_sampling_freq(self, freq):
        raise Exception('this method is not implemented')

    def get_ad_channel(self):
        raise Exception('this method is not implemented')

    def get_da_channel(self):
        raise Exception('this method is not implemented')

    def get_hex_data(self):
        raise Exception('this method is not implemented')

    def set_hex_data(self, data):
        raise Exception('this method is not implemented')

    def get_float_data(self):
        raise Exception('this method is not implemented')

    def set_float_data(self, data):
        raise Exception('this method is not implemented')

    def get_ad_resolution(self):
        raise Exception('this method is not implemented')

    def get_da_resolution(self):
        raise Exception('this method is not implemented')

    def get_ad_range(self):
        raise Exception('this method is not implemented')

    def get_da_range(self):
        raise Exception('this method is not implemented')
