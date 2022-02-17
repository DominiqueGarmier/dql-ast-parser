from __future__ import annotations

from abc import ABC


class DQLExpression(ABC):
    def to_dql(self) -> str:
        '''
        represents ast as a valid dql string
        '''
        raise NotImplementedError()


class DQLAst(DQLExpression):
    content: list[DQLQuery]


class DQLQuery(DQLExpression):
    query_name: str
    query_args: list[DQLVariableDef]


class DQLDirective(DQLExpression):
    pass


class DQLQueryBlock(DQLExpression):
    block_name: str
    arguments: list[int]
    content: list[int]


class DQLVariable(DQLExpression):
    name: str


class DQLVariableDef(DQLExpression):
    var: DQLVariable
    _type: str


class DQLAtrribute(DQLExpression):
    name: str


class DQLAlias:
    alias: str
    maps_to: DQLAtrribute


class DQLKeyword(DQLExpression):
    name: str


def dql_ast() -> DQLAst:
    pass


def read_lines(file_path: str) -> list[str]:
    with open('file_path') as file:
        return file.readlines()
