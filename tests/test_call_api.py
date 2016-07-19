# -*- coding: utf-8 -*-
from six import print_ as print

from .fixture import *
from rqbacktest import StrategyExecutor
from rqbacktest.api import *


def test_import_api():
    from rqbacktest.api import (
        order_shares, order_percent, order_lots, order_value,
        order_target_value, order_target_percent, get_order,
        get_open_orders, cancel_order, update_universe,
        instruments, history, is_st_stock,
    )


def test_instrument(trading_params, data_proxy):
    def init(context):
        context.stocks = []

    def handle_bar(context, bar_dict):
        if len(context.stocks) == 0:
            context.stocks.append(instruments("600485.XSHG"))

    executor = StrategyExecutor(
        init=init,
        handle_bar=handle_bar,

        trading_params=trading_params,
        data_proxy=data_proxy,
    )

    perf = executor.execute()

    i = executor.strategy_context.stocks[0]
    assert i.order_book_id == "600485.XSHG"
