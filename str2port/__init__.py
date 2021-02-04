from .core import StrToPort


def str2port(s, use_iana=False, start=1024, end=65536):
    return StrToPort(s, use_iana, start, end).all()
