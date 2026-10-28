pandas as pd
import numpy as np
import yfinance as yf
import time

st.set_page_config(page_title="Quotex RSI Signal Generator", layout="centered")

st.title("📈 Quotex Live RSI Signal Generator")
st.write("Yeh app live market data (RSI) par mabni signals fraham karti hai.")

# Currency pairs selection
asset = st.selectbox("Select Currency Pair / Asset", ["EURUSD=X", "GBPUSD=X", "USDJPY=X", "AUDUSD=X", "BTC-USD"])

if st.button("Generate Live Signal"):
    with st.spinner('Market data fetch ho ra
                # Calculate RSI
                delta = data['Close'].diff()
                gain = (delta.where(delta > 0, 0)).rolling(window=14).mean()
                loss = (-delta.where(delta < 0, 0)).rolling(window=14).mean()
                rs = gain / loss
                rsi = 100 - (100 / (1 + rs))
                
                current_rsi = float(rsi.iloc[-1].item())
                current_price = float(data['Close'].iloc[-1].item())
                
                st.metric(label="Current Price", value=f"{current_price:.4f}")
                st.metric(label="Current RSI (14)", value=f"{current_2 := current_rsi:.2f}")
                
                # Signal Logic
                st.subheader("Signal Output:")
                if current_rsi < 30:
        
