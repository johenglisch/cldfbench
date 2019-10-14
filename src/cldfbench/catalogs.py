"""
Reference catalogs
"""
from clldutils.misc import lazyproperty

from cldfbench.repository import Repository

try:  # pragma: no cover
    from pyglottolog import Glottolog as GlottologAPI
except ImportError:  # pragma: no cover
    GlottologAPI = 'pyglottolog'

try:  # pragma: no cover
    from pyconcepticon import Concepticon as ConcepticonAPI
except ImportError:  # pragma: no cover
    ConcepticonAPI = 'pyconcepticon'

try:  # pragma: no cover
    from pyclts.api import CLTS as CLTSAPI
except ImportError:  # pragma: no cover
    CLTSAPI = 'pyclts'

__all__ = ['Catalog', 'Glottolog', 'Concepticon', 'CLTS', 'BUILTIN_CATALOGS']


class Catalog(Repository):
    """
    A `Catalog` is a git repository clone (optionally with a python API to access it).
    """
    __api__ = None
    __cli_name__ = None

    def __init__(self, path, tag=None):
        if isinstance(self.__api__, str):
            raise ValueError(
                'API for catalog {0} is not available, please install {1}!'.format(
                    self.__class__.__name__, self.__api__))
        super().__init__(path)
        self._prev_branch = None
        self.tag = tag

    def __enter__(self):
        if self.tag:
            try:
                self._prev_branch = self.repo.active_branch.name
            except TypeError:
                pass
            self.checkout(self.tag)
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self._prev_branch:
            self.checkout(self._prev_branch)

    @classmethod
    def cli_name(cls):
        return cls.__cli_name__ or cls.__name__.lower()

    @lazyproperty
    def api(self):
        if self.__api__:
            return self.__api__(self.dir)


class Glottolog(Catalog):
    __api__ = GlottologAPI


class CLTS(Catalog):
    __api__ = CLTSAPI


class Concepticon(Catalog):
    __api__ = ConcepticonAPI


BUILTIN_CATALOGS = [Glottolog, Concepticon, CLTS]
