import inspect
from dataclasses import dataclass, field, astuple, asdict
from pprint import pprint

@dataclass(frozen=True, order=True)
class Comment:
    id: int = field()
    text: str = field(default="")
    replies: list[int] = field(default_factory=list, hash=False)


def main():
    c = Comment(1, "hey")
    a = {c: "d"} 
    pprint(inspect.getmembers(Comment, inspect.isfunction))
    #c.id = 2
    pprint(dir(c))
    pprint(astuple(c))
    pprint(asdict(c))
    print(id(asdict(c)['replies']))
    print(id([]))


if __name__ == "__main__":
    main()
