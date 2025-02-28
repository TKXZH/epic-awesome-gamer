# -*- coding: utf-8 -*-
# Time       : 2022/1/17 15:20
# Author     : QIN2DIM
# Github     : https://github.com/QIN2DIM
# Description:
from typing import Optional, Sequence


class AwesomeException(Exception):
    def __init__(
        self, msg: Optional[str] = None, stacktrace: Optional[Sequence[str]] = None
    ) -> None:
        self.msg = msg
        self.stacktrace = stacktrace

    def __str__(self) -> str:
        exception_msg = "Message: {}\n".format(self.msg)
        if self.stacktrace:
            stacktrace = "\n".join(self.stacktrace)
            exception_msg += "Stacktrace:\n{}".format(stacktrace)
        return exception_msg


class ContextException(AwesomeException):
    """上下文使用错误"""

    pass


class SwitchContext(ContextException):
    """当使用普通驱动上下文处理人机验证时抛出"""

    pass


class AuthException(AwesomeException):
    """身份认证出现问题时抛出，例如遭遇插入到 hcaptcha 之后的 2FA 身份验证"""

    pass


class PaymentException(AwesomeException):
    """订单操作异常"""

    pass


class PaymentAutoSubmit(PaymentException):
    """点击获取游戏后，订单窗格没有弹出，直接感谢我们购买游戏"""

    pass


class CookieExpired(AwesomeException):
    """身份令牌或饼干过期时抛出"""

    pass


class AssertTimeout(AwesomeException):
    """断言超时"""

    pass


class UnableToGet(AwesomeException):
    """不可抗力因素，游戏无法获取"""

    pass


class SurpriseExit(KeyboardInterrupt):
    """脑洞大开的作者想挑战一下 Python 自带的垃圾回收机制，决定以一种极其垂直的方式结束系统任务。"""

    pass
