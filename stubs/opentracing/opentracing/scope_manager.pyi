from .span import Span

class ScopeManager:
    def __init__(self) -> None: ...
    def activate(self, span: Span, finish_on_close: bool): ...
    @property
    def active(self): ...
