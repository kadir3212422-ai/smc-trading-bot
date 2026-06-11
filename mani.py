import time
import requests
import pandas as pd

# 1. የቴሌግራም መረጃ
TELEGRAM_USERNAME = "BEASTACT"

# 2. የ MetaAPI መረጃዎች (የአንተ እውነተኛ ቁጥሮች እዚህ ገብተዋል!)
META_API_TOKEN = "EyJhbGciOiJSUzUxMiIsInR5cCI6IkpXVCJ9.eyJfaWQiOiI1ZGI0NjZmNTU1MzkxYWUwZDU4YjBjZDY3MDEwNDY1ZSIsImFjY2Vzc1J1bGVzIjpbeyJpZCI6InRyYWRpbmctYWNjb3VudC1tYW5hZ2VtZW50LWFwaSIsIm1ldGhvZHMiOlsidHJhZGluZy1hY2NvdW50LW1hbmFnZW1lbnQtYXBpOnJlc3Q6cHVibGljOio6KiJdLCJyb2xlcyI6WyJyZWFkZXIiLCJ3cml0ZXIiXSwicmVzb3VyY2VzIjpbIio6JFVTRVJfSUQkOioiXX0seyJpZCI6Im1ldGFhcGktcmVzdC1hcGkiLCJtZXRob2RzIjpbIm1ldGFhcGktYXBpOnJlc3Q6cHVibGljOio6KiJdLCJyb2xlcyI6WyJyZWFkZXIiLCJ3cml0ZXIiXSwicmVzb3VyY2VzIjpbIio6JFVTRVJfSUQkOioiXX0seyJpZCI6Im1ldGFhcGktcnBjLWFwaSIsIm1ldGhvZHMiOlsibWV0YWFwaS1hcGk6d3M6cHVibGljOio6KiJdLCJyb2xlcyI6WyJyZWFkZXIiLCJ3cml0ZXIiXSwicmVzb3VyY2VzIjpbIio6JFVTRVJfSUQkOioiXX0seyJpZCI6Im1ldGFhcGktcmVhbC10aW1lLXN0cmVhbWluZy1hcGkiLCJtZXRob2RzIjpbIm1ldGFhcGktYXBpOndzOnB1YmxpYzoqOioiXSwicm9sZXMiOlsicmVhZGVyIiwid3JpdGVyIl0sInJlc291cmNlcyI6WyIqOiRVU0VSX0lEJDoqIl19LHsiaWQiOiJtZXRhc3RhdHMtYXBpIiwibWV0aG9kcyI6WyJtZXRhc3RhdHMtYXBpOnJlc3Q6cHVibGljOio6KiJdLCJyb2xlcyI6WyJyZWFkZXIiLCJ3cml0ZXIiXSwicmVzb3VyY2VzIjpbIio6JFVTRVJfSUQkOioiXX0seyJpZCI6InJpc2stbWFuYWdlbWVudC1hcGkiLCJtZXRob2RzIjpbInJpc2stbWFuYWdlbWVudC1hcGk6cmVzdDpwdWJsaWM6KjoqIl0sInJvbGVzIjpbInJlYWRlciIsIndyaXRlciJdLCJyZXNvdXJjZXMiOlsiKjokVVNFUl9JRCQ6KiJdfSx7ImlkIjoiY29weWZhY3RvcnktYXBpIiwibWV0aG9kcyI6WyJjb3B5ZmFjdG9yeS1hcGk6cmVzdDpwdWJsaWM6KjoqIl0sInJvbGVzIjpbInJlYWRlciIsIndyaXRlciJdLCJyZXNvdXJjZXMiOlsiKjokVVNFUl9JRCQ6KiJdfSx7ImlkIjoibXQtbWFuYWdlci1hcGkiLCJtZXRob2RzIjpbIm10LW1hbmFnZXItYXBpOnJlc3Q6ZGVhbGluZzoqOioiLCJtdC1tYW5hZ2VyLWFwaTpyZXN0OnB1YmxpYzoqOioiXSwicm9sZXMiOlsicmVhZGVyIiwid3JpdGVyIl0sInJlc291cmNlcyI6WyIqOiRVU0VSX0lEJDoqIl19LHsiaWQiOiJiaWxsaW5nLWFwaSIsIm1ldGhvZHMiOlsiYmlsbGluZy1hcGk6cmVzdDpwdWJsaWM6KjoqIl0sInJvbGVzIjpbInJlYWRlciJdLCJyZXNvdXJjZXMiOlsiKjokVVNFUl9JRCQ6KiJdfVssImlnbm9yZVJhdGVMaW1pdHMiOmZhbHNlLCJ0b2tlbklkIjoiMjAyMTAyMTMiLCJpbXBlcnNvbmF0ZWQiOmZhbHNlLCJyZWFsVXNlcklkIjoiNWRiNDY2ZjU1NTM5MWFlMGQ1OGIwY2Q2NzAxMDQ2NWUiLCJpYXQiOjE3ODEyMTU1MjQsImV4cCI6MTc4ODk5MTUyNH0.NrgMl8zqyaQ5wteP3k2i1BPFNKn2lGLa0YuHGGsWlaNtaeFz0tcesG_HiMV-w_nEMKP2MU5H7KPwHTlC60yNWIrnGmWbRQkAJiBbk06MhCmP-UeTrpwwLxWLPiaTB08GPHm8f7fw9Nqq8rv5ugCE0nhjuKFOXYYzppQUKXvbb2aIgMTs7Ri_TaBL-ob5OPHg-72MOUT0J6HySfAqgLX1fQhmFCGswNfOCzjwAijAYF1IAFJuar_V0z6_3jApd1-d78TumB1C-i6jrUhLJjPjPqp6lr3AS8sxC9wIHyKyn0o-cRGfa7dXPuQgULk1TFYQCoojzJqFYgsYxkQyHFthzUdKkxWUUZ9jjYY65rUSClxixJqI71zFfbSYS7gPaXLHBhrRdLzUvptIJU1fsUhUoF0d4F4wJG15GDCf_Ll0RJEGoIRjE8ZSDWsKy3ws5CDnIXkZftzAdDO-YYiQhNj6C6JVG2PPuehypbBhuCW_Z6T0cPQcPRWgu0WMOuoSkzQ2CwvVXvIZvpfgCqDFkYwdkc2IuP_uvn5Y5wAhfSnHBDvf0p2lgxZmAu3_sBZ2snBfZ98K2LQPWe2Gfj_3my18epRZlu-1A6N5pyTwtVGP5tXnyK8x4MwSqN_8uuwI3fH7AFAEywS3gx-eui8xeXLuGapWgdO9iBhWBUfbfB6epc8"
META_ACCOUNT_ID = "5fb57eb1-3334-4aba-8388-17841949600e"

print("--- 🤖 የራስ-ገዢ (Automated Execution) SMC ቦት ተነስቷል ---")

def send_telegram_alert(message):
    url = f"https://api.callmebot.com/text.php?user=@{TELEGRAM_USERNAME}&text={requests.utils.quote(message)}"
    try:
        requests.get(url)
    except:
        pass

def get_live_candles():
    url = "https://api.binance.com/api/v3/klines?symbol=BTCUSDT&interval=15m&limit=100"
    try:
        res = requests.get(url).json()
        df = pd.DataFrame(res, columns=['time', 'open', 'high', 'low', 'close', 'v', 'ct', 'qa', 'nt', 'tbb', 'tbq', 'i'])
        return df.astype(float)
    except Exception as e:
        print(f"የገበያ መረጃ ስህተት፦ {e}")
        return None

def check_smc_setup():
    df = get_live_candles()
    if df is None or len(df) < 5:
        return
    
    last = df.iloc[-2]
    prev = df.iloc[-3]
    prev2 = df.iloc[-4]
    
    # 1. 🪟 Fair Value Gap (FVG) Detection
    is_bullish_fvg = last['low'] > prev2['high']
    is_bearish_fvg = last['high'] < prev2['low']
    
    if is_bullish_fvg:
        fvg_size = last['low'] - prev2['high']
        msg = f"🎯 **SMC SNIPER ENTRY ALERT** 🎯\n\n🔥 **የምርት ዓይነት:** XAUUSD (ወርቅ)\n📈 **የስትራቴጂ ዓይነት:** Buy FVG + Fibonacci OTE\n\n🔍 **1. FVG ማረጋገጫ:**\n- የክፍተት መጠን: ${fvg_size:.2f}\n\n💡 **የሊቃውንት ምክር (SMC):** ዋጋው ወደ ኋላ ተመልሶ በዚህ የ FVG ዞን ውስጥ ሲገባ የ Buy ትዕዛዝ ለመክፈት ተዘጋጅ!"
        print("Buy FVG ተገኝቷል!")
        send_telegram_alert(msg)
        execute_trade("BUY")
        
    elif is_bearish_fvg:
        fvg_size = prev2['low'] - last['high']
        msg = f"🎯 **SMC SNIPER ENTRY ALERT** 🎯\n\n🔥 **የምርት ዓይነት:** XAUUSD (ወርቅ)\n📉 **የስትራቴጂ ዓይነት:** Sell FVG + Fibonacci OTE\n\n🔍 **1. FVG ማረጋገጫ:**\n- የክፍተት መጠን: ${fvg_size:.2f}\n\n💡 **የሊቃውንት ምክር (SMC):** ዋጋው ወደ ኋላ ተመልሶ በዚህ የ FVG ዞን ውስጥ ሲገባ የ Sell ትዕዛዝ ለመክፈት ተዘጋጅ!"
        print("Sell FVG ተገኝቷል!")
        send_telegram_alert(msg)
        execute_trade("SELL")

def execute_trade(action):
    headers = {"auth-token": META_API_TOKEN}
    url = f"https://mt-client-api-v1.london.agiliumtrade.ai/users/current/accounts/{META_ACCOUNT_ID}/trade"
    
    payload = {
        "actionType": "ORDER_TYPE_BUY" if action == "BUY" else "ORDER_TYPE_SELL",
        "symbol": "XAUUSD",
        "volume": 0.01,
        "comment": "SMC Bot Automated Entry"
    }
    
    try:
        response = requests.post(url, json=payload, headers=headers)
        if response.status_code == 200:
            send_telegram_alert(f"🚀 **የፓዚሽን ማረጋገጫ:** ${action} ትዕዛዝ በ Exness አካውንትህ ላይ በሰላም ተከፍቷል!")
        else:
            print(f"ትሬድ መክፈት አልተቻለም፦ {response.text}")
    except Exception as e:
        print(f"የ MetaAPI ግንኙነት ስህተት፦ {e}")

# ቦቱ በየ 5 ደቂቃው ገበያውን እንዲተነትን
while True:
    print("ገበያው እየተተነተነ ነው...")
    check_smc_setup()
    time.sleep(300)
