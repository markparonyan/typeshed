from collections.abc import Iterable

def namedtuple(typename: str, field_names: str | Iterable[str], verbose: bool = False, rename: bool = False): ...
def namedlist(typename: str, field_names: str | Iterable[str], verbose: bool = False, rename: bool = False): ...

__all__ = ["namedlist", "namedtuple"]
