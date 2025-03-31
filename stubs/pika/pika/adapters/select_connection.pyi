import abc
from _typeshed import Incomplete
from logging import Logger

import pika.compat
from pika.adapters.base_connection import BaseConnection
from pika.adapters.utils.selector_ioloop_adapter import AbstractSelectorIOLoop

LOGGER: Logger
SELECT_TYPE: Incomplete

class SelectConnection(BaseConnection):
    def __init__(
        self,
        parameters: Incomplete | None = None,
        on_open_callback: Incomplete | None = None,
        on_open_error_callback: Incomplete | None = None,
        on_close_callback: Incomplete | None = None,
        custom_ioloop: Incomplete | None = None,
        internal_connection_workflow: bool = True,
    ) -> None: ...
    @classmethod
    def create_connection(
        cls, connection_configs, on_done, custom_ioloop: Incomplete | None = None, workflow: Incomplete | None = None
    ): ...

class _Timeout:
    deadline: Incomplete
    callback: Incomplete
    def __init__(self, deadline, callback) -> None: ...
    def __eq__(self, other): ...
    def __ne__(self, other): ...
    def __lt__(self, other): ...
    def __gt__(self, other): ...
    def __le__(self, other): ...
    def __ge__(self, other): ...

class _Timer:
    def __init__(self) -> None: ...
    def close(self) -> None: ...
    def call_later(self, delay, callback): ...
    def remove_timeout(self, timeout) -> None: ...
    def get_remaining_interval(self): ...
    def process_timeouts(self) -> None: ...

class PollEvents:
    READ: Incomplete
    WRITE: Incomplete
    ERROR: Incomplete

class IOLoop(AbstractSelectorIOLoop):
    READ: Incomplete
    WRITE: Incomplete
    ERROR: Incomplete
    def __init__(self) -> None: ...
    def close(self) -> None: ...
    def call_later(self, delay, callback): ...
    def remove_timeout(self, timeout_handle) -> None: ...
    def add_callback_threadsafe(self, callback) -> None: ...
    add_callback: Incomplete
    def process_timeouts(self) -> None: ...
    def add_handler(self, fd, handler, events) -> None: ...
    def update_handler(self, fd, events) -> None: ...
    def remove_handler(self, fd) -> None: ...
    def start(self) -> None: ...
    def stop(self) -> None: ...
    def activate_poller(self) -> None: ...
    def deactivate_poller(self) -> None: ...
    def poll(self) -> None: ...

class _PollerBase(pika.compat.AbstractBase, metaclass=abc.ABCMeta):
    POLL_TIMEOUT_MULT: int
    def __init__(self, get_wait_seconds, process_timeouts) -> None: ...
    def close(self) -> None: ...
    def wake_threadsafe(self) -> None: ...
    def add_handler(self, fileno, handler, events) -> None: ...
    def update_handler(self, fileno, events) -> None: ...
    def remove_handler(self, fileno) -> None: ...
    def activate_poller(self) -> None: ...
    def deactivate_poller(self) -> None: ...
    def start(self) -> None: ...
    def stop(self) -> None: ...
    @abc.abstractmethod
    def poll(self): ...

class SelectPoller(_PollerBase):
    POLL_TIMEOUT_MULT: int
    def poll(self) -> None: ...

class KQueuePoller(_PollerBase):
    def __init__(self, get_wait_seconds, process_timeouts) -> None: ...
    def poll(self) -> None: ...

class PollPoller(_PollerBase):
    POLL_TIMEOUT_MULT: int
    def __init__(self, get_wait_seconds, process_timeouts) -> None: ...
    def poll(self) -> None: ...

class EPollPoller(PollPoller):
    POLL_TIMEOUT_MULT: int
