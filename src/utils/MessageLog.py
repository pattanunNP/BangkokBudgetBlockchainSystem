from sty import Style, RgbFg, fg, bg, ef, rs


class Msg:

    """
    To use this modelue 
    Msg.Warn_print(text: str)
    """
    @staticmethod
    def Warn_print(text):

        text = str(text)
        fg.YELLOW = Style(RgbFg(255, 204, 0))
        Warning_text = fg.YELLOW + text + fg.rs
        print(Warning_text)

    @staticmethod
    def Error_print(text):
        text = str(text)
        fg.RED = Style(RgbFg(255, 100, 0))
        Error_text = fg.RED + text + fg.rs
        print(Error_text)

    @staticmethod
    def Success_print(text):
        text = str(text)
        fg.GREEN = Style(RgbFg(0, 255, 12))
        Success_text = fg.GREEN + text + fg.rs
        print(Success_text)

    @staticmethod
    def Info_print(text):
        text = str(text)
        fg.WHITE = Style(RgbFg(255, 255, 255))
        Info_text = fg.WHITE + text + fg.rs
        print(Info_text)

    @staticmethod
    def Hilight_print(text):
        text = str(text)
        fg.WHITE = Style(RgbFg(102, 205, 255))
        Info_text = fg.WHITE + text + fg.rs
        print(Info_text)
