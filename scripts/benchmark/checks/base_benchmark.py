from abc import (
    ABCMeta,
    abstractmethod,
    abstractproperty
)
import logging
from typing import (
    Any,
    Callable
)

from utils.meters import (
    time_call,
    TimedResult
)
from utils.reporting import (
    DefaultStat,
    print_default_benchmark_result_header,
    print_default_benchmark_stat_line,
    print_default_benchmark_total_line,
)
from utils.shellart import (
    bold_yellow
)


class BaseBenchmark(metaclass=ABCMeta):

    @abstractmethod
    def execute(self) -> DefaultStat:
        raise NotImplementedError(
            "Must be implemented by subclasses"
        )

    @abstractproperty
    def name(self) -> DefaultStat:
        raise NotImplementedError(
            "Must be implemented by subclasses"
        )

    def print_result_header(self) -> None:
        print_default_benchmark_result_header()

    def print_stat_line(self, stat: DefaultStat) -> None:
        print_default_benchmark_stat_line(stat)

    def print_total_line(self, stat: DefaultStat) -> None:
        print_default_benchmark_total_line(stat)

    def run(self) -> DefaultStat:
        logging.info(bold_yellow('Starting benchmark: {}\n'.format(self.name)))
        self.print_result_header()
        stat = self.execute()
        self.print_total_line(stat)
        return stat

    def as_timed_result(self, fn: Callable[..., Any]=None) -> TimedResult:
        return time_call(fn)