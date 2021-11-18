"""
Cryptocurency Daily Prices 
Dashboard using streamlit and Yahoo Finance libraries
@Bek Brace 
Almost the same thing we did with stock prices in previous tutorial
"""

import yfinance as yf  # Yahoo finance to get stock data
import streamlit as st  # Streamlit to create the webapp
from PIL import Image  # Import Pillow to add icons - Python Image Library
from urllib.request import urlopen  # To add URLS


# Define bitcoin and ethereum and other cryptocurrency abbreviation used by Yahoo Finance.
Bitcoin = 'BTC-USD'
Ethereum = 'ETH-USD'
Ripple = 'XRP-USD'
Bitcoin_Cash = 'BCH-USD'


# Lets access the Data from Yahoo Finance using .ticker method
BTC_Data = yf.Ticker(Bitcoin)
ETH_Data = yf.Ticker(Ethereum)
XRP_Data = yf.Ticker(Ripple)
BCH_Data = yf.Ticker(Bitcoin_Cash)


# Lets fetch the Price History from Yahoo Finance. We use Max Period to get all the History
BTCHis = BTC_Data.history(period="max")
ETHHis = ETH_Data.history(period="max")
XRPHis = XRP_Data.history(period="max")
BCHHis = BCH_Data.history(period="max")

st.title(" Cryptocurrency Daily Prices ₿ ")
st.header("Your Dashboard ✨")
st.subheader("You can add more crypto in the code </>")

#Bitcoin
st.write(""" ## Bitcoin ($) """)
# Adding icon for BTC
imageBTC = Image.open(urlopen('https://s2.coinmarketcap.com/static/img/coins/64x64/1.png'))
st.image(imageBTC)
# Create a line chart from BTC-USD Close Price history
st.line_chart(BTCHis.Close,  use_container_width=True)

#Ethereum
st.write(""" ## Ethereum ($) """)
# Adding icon for ETH
imageETH = Image.open(urlopen('https://s2.coinmarketcap.com/static/img/coins/64x64/1027.png'))
st.image(imageETH, use_column_width=False)
# Create a line chart from ETH-USD Close Price history
st.line_chart(ETHHis.Close,  use_container_width=True)

#Ripple
st.write(""" ## Ripple ($) """)
# Adding icon for XRP
imageXRP = Image.open(urlopen('https://s2.coinmarketcap.com/static/img/coins/64x64/52.png'))
st.image(imageXRP, use_column_width=False)
# Create a line chart from XRP-USD Close Price history
st.line_chart(XRPHis.Close,  use_container_width=True)

#Bitcoin Cash
st.write(""" ## Bitcoin-Cash ($USD) """)
# Adding icon for BCH
imageBCH = Image.open(urlopen('https://s2.coinmarketcap.com/static/img/coins/64x64/1831.png'))
st.image(imageBCH, use_column_width=False)
# Create a line chart from BCH-USD Close Price history
st.line_chart(BCHHis.Close,  use_container_width=True)
