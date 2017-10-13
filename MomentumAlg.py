"""
Algorithm investment thesis:
Top-performing stocks will continue to rise due to bullish momentum.
Poor-performing stocks will continue to fall due to bearish momentum.

Every day, we rank S&P500 stocks based on their previous 2 day returns.
We long the top 10% of stocks with the BEST returns over the past 2 days.
We short the top 10% of stocks with the WORST returns over the past 2 days.

We want to buy back shorted shares to avoid the "dead-cat" bounce.
"""

# Import the libraries.
from quantopian.algorithm import attach_pipeline, pipeline_output
from quantopian.pipeline import Pipeline
from quantopian.pipeline.data.builtin import USEquityPricing
from quantopian.pipeline.factors import Returns
from quantopian.pipeline.filters.morningstar import Q1500US

